import requests
from bs4 import BeautifulSoup

def find_series_title_next_epizode(url):
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

if __name__ == "__main__":
    # Пример использования
    series_url = input("Введите URL сериала на Next Epizode: ")
    series_title = find_series_title_next_epizode(series_url)
    print(f"Название сериала: {series_title}")
