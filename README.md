## [Comics pusher](https://github.com/DmitryShvedov88/Comics_pusher "LINK TO THE PROJECT")

This program made for education purpose
It download story from [xkcd](https://xkcd.com/) and send it in telegram chanal
 
This program consists of two parts.
The first part is a two programs that allows you to upload photos on specified topics from xkcd website.
The second part is the publication of them in the Telegram channel.
But you have to start only first one/

### To upload a photo, you are given the opportunity to see what kind of photos they will be, using the necessary program.

First program: 'recive_space_x_photo' enter launch number for a photo from the xkcd Website, if you don't, just start program, you will automatically get the newest.
    
    python recive_story.py 

    example of running:
    python recive_story.py 
    program response:
    Ссылки есть
    Ссылок нет
    Story comment
    

The second part sends photos to the telegram channel. 

### How to check
A folder will be created on the computer in the selected directory and photos will be uploaded there, and delete after push for computer.
The second part sends photos in TG-chanel.

### How to install
Python3 should already be installed.
Use pip (or pip3, if there is a conflict with Python2) to install dependencies.
    
    pip install -r requirements.txt

### environment variables
For the program to function, you will need the following environment variables: TG_TOKEN, CHAT_ID.


TG_TOKEN - is the digital key needed to run TG Bot
You can get it using [Botfather](https://t.me/BotFather) 

CHAT_ID - is a number of chat, where you want to push photo.
It s easy to find it is the name of the bot after @. "@BOT_NAME"

### Project Goals
The code is written for educational purposes on online-course for web-developers dvmn.org.
