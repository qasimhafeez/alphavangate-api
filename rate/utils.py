import requests
import json
from rest_framework.status import HTTP_200_OK


def get_rate():
    url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey=RPECBEU9BGLGO8AN'
    response = requests.get(url)
    if response.status_code == HTTP_200_OK:
        result = json.loads(response.text)['Realtime Currency Exchange Rate']['5. Exchange Rate']
    else:
        result = 'Rate not available'

    return result
