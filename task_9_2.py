import os
import multiprocessing
from pathlib import Path
import time
import requests


task_dir = os.path.join(Path(__file__).resolve().parent, 'task_9')

if not os.path.exists(task_dir):
    os.mkdir(task_dir)

BASE_DIR = os.path.join(task_dir, 'processes')

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


def download_image(url: str):
    response = requests.get(url)
    paths = url.replace('https://', '').split('/')
    dirname, filename = paths[0].replace('.', '_'), paths[-1]

    if not os.path.exists(os.path.join(BASE_DIR, dirname)):
        os.mkdir(os.path.join(BASE_DIR, dirname))

    with open(os.path.join(BASE_DIR, dirname, filename), 'wb') as f:
        f.write(response.content)


def main():
    processes: list[multiprocessing.Process] = []

    start_time = time.time()

    for url in urls:
        process = multiprocessing.Process(target=download_image, args=(url,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print(f'Completed download in {time.time()- start_time} seconds.')


if __name__ == '__main__':
    main()