from datetime import date

import requests

from main.models import Currency


def get_data():
    response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
    currencies = response.json()['Valute']

    for charcode, data in currencies.items():
        currency_obj = Currency(
            charcode=charcode,
            date=date.today(),
            rate=data['Value']
        )
        currency_obj.save()
        