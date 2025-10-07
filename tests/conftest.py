import pytest
import random
import datetime


@pytest.fixture
def time_periods():
    year_1 = random.randint(2000, 2025)
    year_2 = random.randint(2000, 2025)
    month_1 = random.randint(1, 12)
    month_2 = random.randint(1, 12)
    day_1 = random.randint(1, 28)
    day_2 = random.randint(1, 28)
    hour_1 = random.randint(0, 23)
    hour_2 = random.randint(0, 23)
    minutes_1 = random.randint(0, 59)
    minutes_2 = random.randint(0, 59)
    seconds_1 = random.randint(0, 59)
    seconds_2 = random.randint(0, 59)

    date_1 = f'{year_1}-{month_1}-{day_1} {hour_1}:{minutes_1}:{seconds_1}'
    date_2 = f'{year_2}-{month_2}-{day_2} {hour_2}:{minutes_2}:{seconds_2}'
    result_1 = (datetime.datetime(year=year_1, month=month_1, day=1, hour=hour_1, minute=minutes_1, second=seconds_1),
                datetime.datetime(year=year_1, month=month_1, day=day_1,
                                  hour=hour_1, minute=minutes_1, second=seconds_1))
    result_2 = (datetime.datetime(year=year_2, month=month_2, day=1, hour=hour_2, minute=minutes_2, second=seconds_2),
                datetime.datetime(year=year_2, month=month_2, day=day_2,
                                  hour=hour_2, minute=minutes_2, second=seconds_2))

    period_1 = (date_1, result_1)
    period_2 = (date_2, result_2)

    return [period_1, period_2]


@pytest.fixture
def operations_in_period():
    year_1 = random.randint(2000, 2025)
    year_2 = random.randint(2000, 2025)
    month_1 = random.randint(1, 12)
    month_2 = random.randint(1, 12)
    day_1 = random.randint(1, 28)
    day_2 = random.randint(1, 28)
    date_1 = f'{year_1}-{month_1}-{max(day_1, day_2)} 0:0:0'
    date_2 = f'{year_2}-{month_2}-{max(day_1, day_2)} 0:0:0'
    operations = [{'operation_date': f'{day_1}.{month_1}.{year_1} 12:49:53',
                   'payment_date': f'{day_1}.{month_1}.{year_1}',
                   'card_number': None, 'state': 'OK',
                   'operation_amount': -3000.0, 'operation_currency': 'RUB',
                   'payment_amount': -3000.0, 'payment_currency': 'RUB',
                   'cashback': None, 'category': 'Переводы',
                   'mss': None, 'description': 'Линзомат ТЦ Юность', 'bonuses': 0,
                   'investment_rounding': 0, 'amount_rounding': 3000.0},
                  {'operation_date': f'{day_2}.{month_1}.{year_1} 12:49:53',
                   'payment_date': f'{day_2}.{month_1}.{year_1}',
                   'card_number': None, 'state': 'OK',
                   'operation_amount': -3000.0, 'operation_currency': 'RUB',
                   'payment_amount': -3000.0, 'payment_currency': 'RUB',
                   'cashback': None, 'category': 'Переводы',
                   'mss': None, 'description': 'Линзомат ТЦ Юность', 'bonuses': 0,
                   'investment_rounding': 0, 'amount_rounding': 3000.0},
                  {'operation_date': f'{day_1}.{month_2}.{year_2} 12:49:53',
                   'payment_date': f'{day_1}.{month_2}.{year_2}',
                   'card_number': None, 'state': 'OK',
                   'operation_amount': -3000.0, 'operation_currency': 'RUB',
                   'payment_amount': -3000.0, 'payment_currency': 'RUB',
                   'cashback': None, 'category': 'Переводы',
                   'mss': None, 'description': 'Линзомат ТЦ Юность', 'bonuses': 0,
                   'investment_rounding': 0, 'amount_rounding': 3000.0},
                  {'operation_date': f'{day_2}.{month_2}.{year_2} 12:49:53',
                   'payment_date': f'{day_2}.{month_2}.{year_2}',
                   'card_number': None, 'state': 'OK',
                   'operation_amount': -3000.0, 'operation_currency': 'RUB',
                   'payment_amount': -3000.0, 'payment_currency': 'RUB',
                   'cashback': None, 'category': 'Переводы',
                   'mss': None, 'description': 'Линзомат ТЦ Юность', 'bonuses': 0,
                   'investment_rounding': 0, 'amount_rounding': 3000.0}]
    result_1 = [operations[0], operations[1]]
    result_2 = [operations[2], operations[3]]
    inputs_1 = (operations, date_1, result_1)
    inputs_2 = (operations, date_2, result_2)

    return [inputs_1, inputs_2]


@pytest.fixture
def greetings():
    return [('2020-12-20 03:10:10', 'Доброй ночи'),
            ('2020-12-20 09:10:10', 'Доброе утро'),
            ('2020-12-20 13:10:10', 'Добрый день'),
            ('2020-12-20 16:10:10', 'Добрый вечер')]


@pytest.fixture
def cards_info():
    operations = [{'operation_date': '01.01.2018 12:49:53', 'payment_date': '01.01.2018',
                   'card_number': None, 'state': 'OK',
                   'operation_amount': -3000.0, 'operation_currency': 'RUB',
                   'payment_amount': -3000.0, 'payment_currency': 'RUB',
                   'cashback': None, 'category': 'Переводы',
                   'mss': None, 'description': 'Линзомат ТЦ Юность', 'bonuses': 0,
                   'investment_rounding': 0, 'amount_rounding': 3000.0},
                  {'operation_date': '01.01.2018 12:49:53', 'payment_date': '01.01.2018',
                   'card_number': '*1234', 'state': 'OK',
                   'operation_amount': -3000.0, 'operation_currency': 'RUB',
                   'payment_amount': -3000.0, 'payment_currency': 'RUB',
                   'cashback': None, 'category': 'Переводы',
                   'mss': None, 'description': 'Линзомат ТЦ Юность', 'bonuses': 0,
                   'investment_rounding': 0, 'amount_rounding': 3000.0}]
    cards = [{"last_digits": None,
              "total_spent": 3000,
              "cashback": 30.0},
             {'last_digits': '1234',
              "total_spent": 3000,
              "cashback": 30.0}]

    return operations, cards
