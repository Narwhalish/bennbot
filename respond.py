#!/usr/bin/python
# -*- encoding: utf-8 -*-

# to load env variables
from dotenv import load_dotenv
# to access env variables
from os import getenv
# to process HTTP requests
import requests

# load env variables from .env file
load_dotenv(verbose=True)

# constants
ACCESS_TOKEN = getenv('ACCESS_TOKEN')
BOT_ID = getenv('BOT_ID')
GROUP_ID = getenv('GROUP_ID')

# request_params
request_params = {'token': ACCESS_TOKEN}

# post_params
post_params = {'bot_id': BOT_ID}

while True:
    # prompt user
    print('Enter message:')

    # prompt for string to send
    message = str(input())
    post_params['text'] = message

    if message.lower() == 'quit':
        break

    # post message to groupchat
    requests.post('https://api.groupme.com/v3/bots/post', params=post_params)
