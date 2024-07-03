import re
from typing import List

import requests
import telegram
from bs4 import BeautifulSoup
from the_python_bay import tpb
from celery.utils.log import get_task_logger
from transmission_rpc import Client, Torrent

from celery_app.celery_settings import app
from jwt_project.models import Link, KnownEpisode
from jwt_project.settings import TRANSMISSION_HOST, TRANSMISSION_PORT, TRANSMISSION_USERNAME, TRANSMISSION_PASSWORD, \
    TELEGRAM_BOT_TOKEN

logger = get_task_logger(__name__)

default_headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/89.0.4356.6 Safari/537.36',
    'Accept-Encoding': ', '.join(('gzip', 'deflate')),
    'Accept': '*/*',
    'Connection': 'keep-alive',
}


def get_show_name_by_url(url):
    response = requests.get(url, headers=default_headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        title_element = soup.find('div', id='show_name')

        if title_element:
            return 0, title_element.text.strip()
        else:
            return 1, "Название сериала не найдено"
    else:
        return 1, f"Ошибка при запросе страницы: {response.status_code}"


@app.task
def add_download_task():
    print("add download task hello")
    for link in Link.objects.exclude(show_name__exact=""):
        link_episodes = KnownEpisode.objects.filter(link=link)
        if not link_episodes:
            episode = KnownEpisode.objects.create(link=link)
            yield_data(episode)
        else:
            last_episode = link_episodes.last()
            if check_if_last(last_episode):
                print("episode is last!")
                continue
            episode = KnownEpisode.objects.create(link=link)
            yield_data(episode)


def check_is_video(file):
    return file.name.endswith('.mkv') or file.name.endswith('.mp4')


def send_file_to_telegram(filepath, userid):
    bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)
    bot.send_document(chat_id=userid, document=open(filepath, 'rb'))


@app.task
def send_downloaded_torrent():
    client = Client(
        host=TRANSMISSION_HOST,
        port=TRANSMISSION_PORT,
        username=TRANSMISSION_USERNAME,
        password=TRANSMISSION_PASSWORD
    )
    for episode in KnownEpisode.objects.filter(is_downloaded=False).exclude(torrent_hash__exact=""):
        torrent = client.get_torrent(episode.torrent_hash)
        if torrent.status == 'seeding':
            episode.is_downloaded = True
            episode.save()
            print(f"Torrent downloaded: {torrent.name}")
            for file_name in filter(check_is_video, torrent.get_files()):
                filepath = torrent.download_dir + file_name.name
                userid = episode.link.user.profile.telegram_id
                send_file_to_telegram(filepath, userid)


def format_search_query(series_title):
    return re.sub(r'[^\w\s]', '', series_title).replace(' ', '.')


print("Successfully connected to Transmission")


def yield_data(episode):
    client = Client(
        host=TRANSMISSION_HOST,
        port=TRANSMISSION_PORT,
        username=TRANSMISSION_USERNAME,
        password=TRANSMISSION_PASSWORD
    )
    show_name = episode.link.show_name
    last_episode = get_last_episode(show_name)
    print("LAST EPISODE", last_episode)
    if not last_episode:
        print(f"No torrents found for query: {show_name}")
        return None
    torrent_url = str(last_episode[2])
    episode.torrent_hash = client.add_torrent(torrent_url).info_hash
    print("TORRENT HASH", episode.torrent_hash)
    episode.season = last_episode[0]
    episode.episode = last_episode[1]
    episode.save()
    print(f"Torrent added: {torrent_url}")
    return episode


def check_if_last(episode):
    last_episode = get_last_episode(episode.link.show_name)
    if not last_episode:
        print(f"No torrents found for query: {episode.link.show_name}")

    if episode.season == last_episode[0] and episode.episode == last_episode[1]:
        return True
    return False


def get_last_episode(show_name):
    search_query = format_search_query(show_name)
    results: List[Torrent] = tpb.search(search_query)
    if results:
        pattern = re.compile(rf"{re.escape(search_query)}.*S(\d{{2}})E(\d{{2}})", re.IGNORECASE)
        episodes = []

        for result in results:
            match = pattern.search(result.name)
            if match:
                season = int(match.group(1))
                episode = int(match.group(2))
                episodes.append((season, episode, result.magnet))

        if episodes:
            episodes.sort(key=lambda x: (x[0], x[1]), reverse=True)
            last_episode = episodes[0]
            return last_episode
    return None
