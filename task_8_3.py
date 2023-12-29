import os
import aiohttp
import asyncio
from pathlib import Path
import time


BASE_DIR = Path(__file__).resolve().parent
saves_dir = os.path.join(BASE_DIR, 'saves')

if not os.path.exists(saves_dir):
    os.mkdir(saves_dir)

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


async def download_content(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            filename = (
                url.replace('https://', '').replace('.', '_').replace('/', '-')
                + '_async.html'
            )
            with open(
                os.path.join(saves_dir, filename), 'w', encoding='utf-8'
            ) as f:
                f.write(await response.text())


async def main():
    tasks = []

    for url in urls:
        task = asyncio.ensure_future(download_content(url))
        tasks.append(task)

    await asyncio.gather(*tasks)



if __name__ == '__main__':
    start_time = time.time()
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())
    print(f'Completed download in {time.time()- start_time} seconds.')