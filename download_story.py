from pathlib import Path
import requests


def download_story(name, photo_format, down_load_link):
    """Download sory from web site"""
    filename = f'number {name}.{photo_format}'
    path = Path(f"story/{filename}")
    path.parent.mkdir(parents=True, exist_ok=True)
    response = requests.get(down_load_link, timeout=10)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)
    return path
