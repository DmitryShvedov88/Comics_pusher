import telegram
import os


def takefiles(directory):
    """Take photos from directory on your computer"""
    filesindir = os.listdir(directory)
    name = os.path.join(*filesindir)
    image = os.path.join(str(directory), name)
    return image


def send_photos(tg_token, chat_id, directory):
    """Push photos in TG Bot Chat"""
    bot = telegram.Bot(token=tg_token)
    image = takefiles(directory)
    with open(image, 'rb') as img:
        bot.send_document(chat_id=chat_id, document=img)
