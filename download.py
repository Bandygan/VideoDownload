from pytube import YouTube


def download_video(url, output_path='.'):
    try:
        # Создаем объект YouTube
        yt = YouTube(url)

        # Выбираем наилучшее качество видео
        stream = yt.streams.get_highest_resolution()

        # Скачиваем видео
        stream.download(output_path)

        print(f"Видео '{yt.title}' успешно скачано в {output_path}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    video_url = input("Введите ссылку на видео: ")
    download_path = input("Введите путь для сохранения видео (по умолчанию текущая папка): ")

    if not download_path:
        download_path = '.'

    download_video(video_url, download_path)
