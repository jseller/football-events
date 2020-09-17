from flask import json

import requests

# get from config
token = '74db8efa2a6db279393b433d97c2bc843f8e32b0'


def scoreboard_data(from_date, to_date):
    api_url = 'https://delivery.chalk247.com/scoreboard/' \
              'NFL/%s/%s.json?api_key=%s' % (
               from_date, to_date, token)
    response = requests.get(api_url)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None


def ranking_data():
    api_url = 'https://delivery.chalk247.com/team_rankings/NFL.json?api_key=%s' % (token)
    response = requests.get(api_url)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None
