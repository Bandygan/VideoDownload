import requests
from bs4 import BeautifulSoup
from transmission_rpc import Client
from the_python_bay import tpb
import re

# Настройки Transmission
TRANSMISSION_HOST = 'localhost'
TRANSMISSION_PORT = 9091
TRANSMISSION_USERNAME = 'VorVZakone'
TRANSMISSION_PASSWORD = '1234'

def find_series_title_next_episode(url):
    # Отправляем GET запрос на указанный URL
    response = requests.get(url)

    # Проверяем успешность запроса
    if response.status_code == 200:
        # Создаем объект BeautifulSoup для парсинга HTML
        soup = BeautifulSoup(response.content, 'html.parser')

        # Находим элемент с названием сериала на Next Epizode
        title_element = soup.find('div', id='show_name')

        if title_element:
            # Извлекаем текст названия сериала
            series_title = title_element.text.strip()
            return series_title
        else:
            return "Название сериала не найдено"
    else:
        return f"Ошибка при запросе страницы: {response.status_code}"

def format_search_query(series_title):
    # Заменяем пробелы на точки и убираем специальные символы
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
            # Фильтруем результаты, чтобы найти эпизоды сериала
            pattern = re.compile(rf"{re.escape(search_query)}.*S(\d{{2}})E(\d{{2}})", re.IGNORECASE)
            episodes = []

            for result in results:
                match = pattern.search(result.name)
                if match:
                    season = int(match.group(1))
                    episode = int(match.group(2))
                    episodes.append((season, episode, result.magnet))

            if episodes:
                # Сортируем эпизоды по номеру сезона и эпизода, чтобы найти последний эпизод
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

if __name__ == "__main__":
    series_url = input("Введите URL сериала на Next Epizode: ")
    series_title = find_series_title_next_episode(series_url)
    print(f"Название сериала: {series_title}")

    if "Ошибка" not in series_title:
        download_last_episode(series_title)
    else:
        print(series_title)
