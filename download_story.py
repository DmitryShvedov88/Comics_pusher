import requests
from pathlib import Path


def make_dir(filename):
    """Creates a directory if it doesn't exist yet"""
    path = Path(f"story/{filename}")
    path.parent.mkdir(parents=True, exist_ok=True)
    return path


def download_story(name, photo_format, down_load_link):
    """Download sory from web site"""
    response = requests.get(down_load_link, timeout=10)
    response.raise_for_status()
    filename = f'number {name}.{photo_format}'
    story_path = make_dir(filename)
    with open(story_path, 'wb') as file:
        file.write(response.content)
    return story_path
