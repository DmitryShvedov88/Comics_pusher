import requests
import random
import os
from download_story import download_story
from story_pusher import send_photos

FIRST_COMICS = 1
LAST_COMICS = 2901


def take_story():
    """Take a comics link"""
    comix_numder = random.randrange(FIRST_COMICS, LAST_COMICS)
    python_story = f"https://xkcd.com/{comix_numder}/info.0.json"
    response = requests.get(python_story, timeout=10)
    response.raise_for_status()
    page_payload = response.json()
    link = page_payload["img"]
    photo_name = page_payload["num"]
    comment = page_payload["alt"]
    photo_format = "jpeg"
    if not link:
        print("Ссылок нет")
        return
    print("Ссылки есть")
    print(comment)
    story = download_story(photo_name, photo_format, link)
    return story


if __name__ == "__main__":
    try:
        story = take_story()
        send_photos()
        os.remove(story)
    finally:
        os.remove(story)