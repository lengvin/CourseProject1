import os
import requests
from dotenv import load_dotenv


load_dotenv()

api_key = os.getenv("API_KEY")
headers = {"apikey": f"{api_key}"}


def currency_conversion_in_rub(operation):
    """
    Конвертация валюты в рубли
    """
    currency = operation['operation_currency']
    amount = operation['operation_amount']

    if currency == "RUB":
        return amount
    else:
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"

        response = requests.get(url, headers=headers)
        response_data = response.json()
        result = response_data["result"]

        return result


def get_currency_rate(user_settings):
    """
    Вывод заданных курсов валют
    """
    result = []
    for currency in user_settings:
        url = f"https://api.apilayer.com/exchangerates_data/latest?symbols=RUB&base={currency}"
        response = requests.get(url, headers=headers)
        response_data = response.json()
        currency_rate = {'currency': currency,
                         'rate': response_data['rates']['RUB']}
        result.append(currency_rate)

    return result
