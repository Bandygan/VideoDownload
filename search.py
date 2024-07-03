import requests
from bs4 import BeautifulSoup
from transmission_rpc import Client
from the_python_bay import tpb
import re

TRANSMISSION_HOST = ''
TRANSMISSION_PORT = 9091
TRANSMISSION_USERNAME = 'VorVZakone'
TRANSMISSION_PASSWORD = '1234'
STATUS_FOUND = 0
STATUS_NOT_FOUND = 1


def find_series_title_next_episode(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        title_element = soup.find('div', id='show_name')

        if title_element:
            series_title = title_element.text.strip()
            return 0, series_title
        else:
            return 1, "Название сериала не найдено"
    else:
        return 1, f"Ошибка при запросе страницы: {response.status_code}"


def format_search_query(series_title):
    return re.sub(r'[^\w\s]', '', series_title).replace(' ', '.')


def download_last_episode(series_title):
    try:
        client = Client(
            host=TRANSMISSION_HOST,
            port=TRANSMISSION_PORT,
            username=TRANSMISSION_USERNAME,
            password=TRANSMISSION_PASSWORD
        )
        print("Successfully connected to Transmission")

        search_query = format_search_query(series_title)
        results = tpb.search(search_query)
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
                torrent_url = str(last_episode[2])
                client.add_torrent(torrent_url)
                print(f"Torrent added: {torrent_url}")
            else:
                print(f"No matching torrents found for query: {search_query}")
        else:
            print(f"No torrents found for query: {search_query}")

    except Exception as e:
        print(f"Failed to connect or add torrent: {e}")


default_headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/89.0.4356.6 Safari/537.36',
    'Accept-Encoding': ', '.join(('gzip', 'deflate')),
    'Accept': '*/*',
    'Connection': 'keep-alive',
}


if __name__ == "__main__":
    series_url = input("Введите URL сериала на Next Epizode: ")
    series_title = find_series_title_next_episode(series_url)
    print(f"Название сериала: {series_title}")

    if "Ошибка" not in series_title:
        download_last_episode(series_title)
    else:
        print(series_title)
