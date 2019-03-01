#/usr/bin/python
# -*- encoding: utf-8 -*-

# to load env variables
from dotenv import load_dotenv
# to access env variables
from os import getenv
# to process HTTP requests
import requests
# to pretty print json
import json
# to prevent bot from being overwhelmed
import time
# meme dispenser
# import memes

# load env variables from .env file
load_dotenv(verbose=True)

# constants
ACCESS_TOKEN = getenv('ACCESS_TOKEN')
BOT_ID = getenv('BOT_ID')
GROUP_ID = getenv('GROUP_ID')

# request_params
request_params = {'token': ACCESS_TOKEN}

# on startup, refresh the since_id parameter
response = requests.get(f'http://api.groupme.com/v3/groups/{GROUP_ID}/messages', params=request_params)
response_messages = response.json()['response']['messages']
request_params['since_id'] = response_messages[0]['id']

# get live chats from the groupchat
while True:
    # get next chat update
    response = requests.get(f'http://api.groupme.com/v3/groups/{GROUP_ID}/messages', params=request_params)
    # if there are new messages
    if (response.status_code == 200):
        # gets and converts recent messages to json
        response_messages = response.json()['response']['messages']

        # iterates through recent messages and respond to anyone who says quack
        for msg in response_messages:
            if (msg['text'].lower() == 'quack'):
                # print(msg['text'])
                post_params = {'bot_id': BOT_ID, 'text': 'quack'}
                if (msg['sender_type'] != 'bot'):
                    # post message to group
                    requests.post('https://api.groupme.com/v3/bots/post', params=post_params)
                # update latest message id
                request_params['since_id'] = response_messages[0]['id']

    # sleep for N seconds
    time.sleep(1.25)
