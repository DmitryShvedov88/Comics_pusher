import telegram
import os
from dotenv import load_dotenv, find_dotenv


def takefiles(directory):
    """Take photos from directory on your computer"""
    images = []
    filesindir = os.listdir(directory)
    for filesindirs in filesindir:
        name = os.path.join(filesindirs)
        path = os.path.join(str(directory), name)
        images.append(path)
    return images


def delete_story(path):
    """Del story form directory"""
    os.remove(path)


def send_photos(story):
    """Push photos in TG Bot Chat"""
    load_dotenv(find_dotenv())
    tg_token = os.getenv("TG_TOKEN")
    chat_id = os.getenv("CHAT_ID")
    directory = os.getenv("DIRECTORY")
    bot = telegram.Bot(token=tg_token)
    image = takefiles(directory)
    with open(*image, 'rb') as img:
        bot.send_document(chat_id=chat_id, document=img)
    delete_story(story)
