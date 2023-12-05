import requests


def get_currency_rate(currency):
    url = f'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/{currency}/rub.json'

    try:
        response = requests.get(url)
        currency = response.json()['rub']
        return currency
    except (requests.RequestException, ValueError, KeyError):
        return None
