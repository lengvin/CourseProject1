import pandas as pd
import datetime
from external_api import currency_conversion_in_rub
import json


def read_excel_file(file_path):
    """
    Преобразование EXCEL-файла в Python-объект
    """
    list_of_keys = ['operation_date',
                    'payment_date',
                    'card_number',
                    'state',
                    'operation_amount',
                    'operation_currency',
                    'payment_amount',
                    'payment_currency',
                    'cashback',
                    'category',
                    'mss',
                    'description',
                    'bonuses',
                    'investment_rounding',
                    'amount_rounding']
    df = pd.read_excel(file_path)
    result = []

    for index, row in df.iterrows():
        result_dict = {}
        iter_list = iter(list_of_keys)

        for key, value in row.items():
            if pd.notna(value):
                result_dict[next(iter_list)] = value
            else:
                result_dict[next(iter_list)] = None

        result.append(result_dict)

    return result


def read_json_file(file_path):
    """
    Преобразование JSON файла в Python-объект
    """
    try:
        with open(file_path, encoding="utf-8") as file:
            json_file = json.load(file)
    except (FileNotFoundError, TypeError, json.JSONDecodeError, ValueError):
        return []
    else:
        return json_file


def get_time_period(date):
    """
    Создание периода времени по конечному значению
    """
    date_and_time = date.split(' ')
    date_list = date_and_time[0].split('-')
    time_list = date_and_time[1].split(':')
    start_date = datetime.datetime(year=int(date_list[0]),
                                   month=int(date_list[1]),
                                   day=1,
                                   hour=0,
                                   minute=0,
                                   second=0)
    end_date = datetime.datetime(year=int(date_list[0]),
                                 month=int(date_list[1]),
                                 day=int(date_list[2]),
                                 hour=int(time_list[0]),
                                 minute=int(time_list[1]),
                                 second=int(time_list[2]))

    return start_date, end_date


def get_operations_in_period(operations, date):
    """
    Выборка операций с начала месяца по указанную дату
    """
    result = []
    start_date, end_date = date
    for operation in operations:
        date_list = operation['operation_date'].split(' ')[0].split('.')
        operation_date = datetime.datetime(year=int(date_list[2]),
                                           month=int(date_list[1]),
                                           day=int(date_list[0]))
        if not (start_date.year <= operation_date.year <= end_date.year):
            continue
        elif not (start_date.month <= operation_date.month <= end_date.month):
            continue
        elif not (start_date.day <= operation_date.day <= end_date.day):
            continue
        else:
            result.append(operation)

    return result


def get_greetings_by_date(date):
    """
    Определение приветствия по секущему времени
    """
    time = date.split(' ')[1].split(':')
    current_time = datetime.datetime(year=1,
                                     month=1,
                                     day=1,
                                     hour=int(time[0]),
                                     minute=int(time[1]),
                                     second=int(time[2]))

    if 4 <= current_time.hour <= 11:
        return 'Доброе утро'
    elif 12 <= current_time.hour <= 15:
        return 'Добрый день'
    elif 16 <= current_time.hour <= 22:
        return 'Добрый вечер'
    else:
        return 'Доброй ночи'


def get_cards_info(operations):
    """
    Получение информации о карте, её суммы трат за период времени и кэшбека
    """
    result = []
    viewed_cards = []
    for operation in operations:
        if operation['card_number'] in viewed_cards:
            continue

        if bool(operation['card_number']):
            viewed_cards.append(operation['card_number'])
            card_number = operation['card_number'][1:]
        else:
            card_number = None
            viewed_cards.append(card_number)
        spends = [currency_conversion_in_rub(x) for x in operations if x['card_number'] == operation['card_number']]
        spends_sum = round(abs(sum(spends)))
        cashback = round(spends_sum / 100, 2)

        card = {'last_digits': card_number,
                'total_spent': spends_sum,
                'cashback': cashback}
        result.append(card)

    return result
