import requests
import random
from download_story import download_story
from story_pusher import send_photos


def take_story():
    """Take a comics link"""
    comix_numder = random.randrange(1, 2901)
    python_story = f"https://xkcd.com/{comix_numder}/info.0.json"
    response = requests.get(python_story, timeout=10)
    response.raise_for_status()
    story = response.json()
    link, photo_name, comment = story["img"], story["num"], story["alt"]
    photo_format = "jpeg"
    if not link:
        print("Ссылок нет")
        return
    print("Ссылки есть")
    print(comment)
    story = download_story(photo_name, photo_format, link)
    return story


if __name__ == "__main__":
    story = take_story()
    send_photos(story)
