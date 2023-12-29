import os
import aiohttp
import asyncio
import aiofiles
from pathlib import Path
import time


task_dir = os.path.join(Path(__file__).resolve().parent, 'task_9')

if not os.path.exists(task_dir):
    os.mkdir(task_dir)

BASE_DIR = os.path.join(task_dir, 'async')

if not os.path.exists(BASE_DIR):
    os.mkdir(BASE_DIR)

urls = [
    'https://i.imgur.com/vfiefI0.jpeg',
    'https://i.imgur.com/qcoE5I9.png',
    'https://i.imgur.com/VTWTeCF.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Stray_kitten_Rambo002.jpg/1200px-Stray_kitten_Rambo002.jpg',
    'https://upload.wikimedia.org/wikipedia/ru/thumb/8/8b/AC-DC_-_Highway_to_Hell.jpg/220px-AC-DC_-_Highway_to_Hell.jpg',
    'https://onrockwave.com/wp-content/uploads/2022/04/orw_071-1-350x250.jpg',
    'https://cloud4box.com/wp-content/uploads/python-300x161.jpg',
]


async def download_image(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            paths = url.replace('https://', '').split('/')
            dirname, filename = paths[0].replace('.', '_'), paths[-1]

            if not os.path.exists(os.path.join(BASE_DIR, dirname)):
                os.mkdir(os.path.join(BASE_DIR, dirname))

            async with aiofiles.open(
                os.path.join(BASE_DIR, dirname, filename), 'wb'
            ) as f:
                await f.write(await response.content.read())


async def main():
    tasks = []

    for url in urls:
        task = asyncio.ensure_future(download_image(url))
        tasks.append(task)

    await asyncio.gather(*tasks)


if __name__ == '__main__':
    start_time = time.time()
    asyncio.run(main())
    print(f'Completed download in {time.time()- start_time} seconds.')