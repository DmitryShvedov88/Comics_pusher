import requests
from pathlib import Path


def download_story(name, photo_format, down_load_link):
    filename = f'number {name}.{photo_format}'
    path = Path(f"story/{filename}")
    path.parent.mkdir(parents=True, exist_ok=True)
    response = requests.get(down_load_link)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)
