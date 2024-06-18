from transmission_rpc import Client
from the_python_bay import tpb

TRANSMISSION_HOST = 'localhost'
TRANSMISSION_PORT = 9091
TRANSMISSION_USERNAME = 'VorVZakone'
TRANSMISSION_PASSWORD = '1234'


def download_tor(search_query):
    try:
        client = Client(
            host=TRANSMISSION_HOST,
            port=TRANSMISSION_PORT,
            username=TRANSMISSION_USERNAME,
            password=TRANSMISSION_PASSWORD
        )
        print("Successfully connected to Transmission")

        results = tpb.search(search_query)
        if results:
            tor = results.pop().magnet
            torrent_url = str(tor)
            client.add_torrent(torrent_url)
            print(f"Torrent added: {torrent_url}")
        else:
            print(f"No torrents found for query: {search_query}")

    except Exception as e:
        print(f"Failed to connect or add torrent: {e}")


if __name__ == "__main__":
    search_query = input("Введите поисковый запрос для торрентов: ")
    download_tor(search_query)
