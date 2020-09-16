import logging

from flask import json

import requests


def scoreboard_data(from_date, to_date, token):
    api_url = 'https://delivery.chalk247.com/scoreboard/' \
              'NFL/%s/%s.json?api_key=%s' % (
               from_date, to_date, token)
    response = requests.get(api_url)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        logging.info(response.status_code)
        return None


def ranking_data(token):
    api_url = 'https://delivery.chalk247.com/team_rankings/NFL.json?api_key=%s' % (token)
    response = requests.get(api_url)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        logging.info(response.status_code)
        return None
