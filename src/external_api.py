import os

import requests
from dotenv import load_dotenv

load_dotenv()

currency_api_key = os.getenv("CURRENCY_API_KEY")
share_api_key = os.getenv("SHARE_API_KEY")
currency_headers = {"apikey": f"{currency_api_key}"}


def get_user_currency_rate(user_settings):
    """
    Вывод курсов заданных валют
    """
    result = []
    for currency in user_settings:
        url = f"https://api.apilayer.com/exchangerates_data/latest?symbols=RUB&base={currency}"
        response = requests.get(url, headers=currency_headers)
        response_data = response.json()
        currency_rate = {"currency": currency, "rate": response_data["rates"]["RUB"]}
        result.append(currency_rate)

    return result


def get_user_stock_prices(user_settings):
    """
    Вывод стоимости заданных акций
    """
    result = []
    for share in user_settings:
        url = f"https://financialmodelingprep.com/stable/profile?symbol={share}&apikey={share_api_key}"
        response = requests.get(url)
        response_data = response.json()
        stock_price = {"stock": share, "price": response_data[0]["price"]}
        result.append(stock_price)

    return result
