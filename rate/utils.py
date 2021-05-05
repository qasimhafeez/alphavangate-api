import json
import os

import requests
from rest_framework.status import HTTP_200_OK
from .models import BtcRate


def get_rate():
    api_key = os.getenv('API_KEY')
    url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey={api_key}'
    response = requests.get(url)
    if response.status_code == HTTP_200_OK:
        result = json.loads(response.text)['Realtime Currency Exchange Rate']['5. Exchange Rate']
    else:
        result = 'Rate not available'

    return result


def get_rate_from_db():
    return BtcRate.objects.last().exchange_rate
