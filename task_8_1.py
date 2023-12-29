import os
import time
import threading
from pathlib import Path
import requests


BASE_DIR = os.path.join(Path(__file__).resolve().parent, 'task_8')

if not os.path.exists(BASE_DIR):
    os.mkdir(BASE_DIR)

urls = [
    'https://ya.ru',
    'https://github.com/DispenserBro',
    'https://google.com',
    'https://gb.ru',
    'https://mail.ru',
    'https://www.python.org/',
    'https://habr.com/ru/all/',
    'https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0',
    'https://news.vtomske.ru/',
    'https://www.1tv.ru/',
]


def download_content(url: str):
    response = requests.get(url)
    filename = (
        url.replace('https://', '').replace('.', '_').replace('/', '-')
        + '_thread.html'
    )
    with open(os.path.join(BASE_DIR, filename), 'w', encoding='utf-8') as f:
        f.write(response.text)


threads: list[threading.Thread] = []


start_time = time.time()

for url in urls:
    thread = threading.Thread(target=download_content, args=[url])
    threads.append(thread)
    thread.start()


for thread in threads:
    thread.join()

print(f'Completed download in {time.time() - start_time} seconds.')