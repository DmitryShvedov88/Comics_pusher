import telegram
import os
from dotenv import load_dotenv, find_dotenv


def takefiles(directory):
    """Take photos from directory on your computer"""
    images = []
    filesindir = os.listdir(directory)
    name = os.path.join(*filesindir)
    path = os.path.join(str(directory), name)
    images.append(path)
    return images


def send_photos():
    """Push photos in TG Bot Chat"""
    load_dotenv(find_dotenv())
    tg_token = os.getenv("TG_TOKEN")
    chat_id = os.getenv("CHAT_ID")
    directory = os.getenv("DIRECTORY")
    bot = telegram.Bot(token=tg_token)
    image = takefiles(directory)
    with open(*image, 'rb') as img:
        bot.send_document(chat_id=chat_id, document=img)
