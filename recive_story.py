import requests
from download_story import download_story


def take_links() -> list:
    python_story = f"https://xkcd.com/1/info.0.json"
    response = requests.get(python_story)
    response.raise_for_status()
    story = response.json()
    #print(story)
    link = story["img"]
    num = story["num"]
    photo_name, photo_format = num, "jpeg"
    comment = story["alt"]
    if not link:
        print("Ссылок нет")
        return
    print("Ссылки есть")
    print(comment)
    download_story(photo_name, photo_format, link)


if __name__ == "__main__":
    take_links()
