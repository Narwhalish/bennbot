#!/usr/bin/python
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

# load env variables from .env file
load_dotenv(verbose=True)

# constants
ACCESS_TOKEN = getenv('ACCESS_TOKEN')
BOT_ID = getenv('BOT_ID')
GROUP_ID = getenv('GROUP_ID')

# request_params
request_params = {'token': ACCESS_TOKEN}

response = requests.get('https://api.imgflip.com/get_memes')
memes = response.json()['data']['memes']
print(json.dumps(response.json(), indent=2, sort_keys=True), response.status_code)


test_meme = memes[0]['url']
print(test_meme)
# groupme_meme = requests.post('')
