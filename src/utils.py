import datetime
import json
import logging
from collections import Counter

import pandas as pd

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(filename)s - %(levelname)s - %(message)s",
    filename="../logs/utils.log",
    filemode="w",
)
module_logger = logging.getLogger(__name__)


def read_excel_file(file_path):
    """
    Преобразование EXCEL-файла в Python-объект
    """
    list_of_keys = [
        "operation_date",
        "payment_date",
        "card_number",
        "state",
        "operation_amount",
        "operation_currency",
        "payment_amount",
        "payment_currency",
        "cashback",
        "category",
        "mss",
        "description",
        "bonuses",
        "investment_rounding",
        "amount_rounding",
    ]
    try:
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

        module_logger.info("Создание Python-объекта из XLSX-файла с операциями пользователя")
    except Exception as e:
        module_logger.error(f"Произошла ошибка: {e}")
    else:
        return result


def read_json_file(file_path):
    """
    Преобразование JSON файла в Python-объект
    """
    try:
        with open(file_path, encoding="utf-8") as file:
            json_file = json.load(file)

        module_logger.info("Создание Python-объекта из JSON-файла")
    except (FileNotFoundError, TypeError, json.JSONDecodeError, ValueError) as e:
        module_logger.error(f"Произошла ошибка: {e}")

        return []
    else:
        return json_file


def get_time_period(date, period="M"):
    """
    Создание периода времени по конечному значению
    """
    try:
        end_date = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
        module_logger.info("Создание начальной точки временного периода")
        start_date = end_date
        if period == "M":
            start_date = start_date.replace(day=1)
        elif period == "W":
            start_date -= datetime.timedelta(days=7)
        elif period == "Y":
            start_date = start_date.replace(year=end_date.year - 1)
        elif period == "ALL":
            start_date = None
        module_logger.info("Создание конечной точки временного периода")
    except Exception as e:
        module_logger.error(f"Произошла ошибка: {e}")
    else:
        return start_date, end_date


def get_operations_in_period(operations, date, period):
    """
    Выборка операций с начала месяца по указанную дату
    """
    try:
        result = []
        start_date, end_date = get_time_period(date, period=period)
        module_logger.info("Начало выборки операций по дате")
        if not (bool(start_date)):
            start_date = int(bool(start_date))
        for operation in operations:
            if not bool(operation["payment_date"]):
                continue
            operation_date = datetime.datetime.strptime(operation["payment_date"], "%d.%m.%Y")
            if not (start_date.year <= operation_date.year <= end_date.year):
                continue
            elif not (start_date.month <= operation_date.month <= end_date.month):
                continue
            elif not (start_date.day <= operation_date.day <= end_date.day):
                continue
            else:
                result.append(operation)
        module_logger.info("Конец выборки операций по дате")
    except Exception as e:
        module_logger.error(f"Произошла ошибка: {e}")
    else:
        return result


def get_greetings_by_date(date):
    """
    Определение приветствия по секущему времени
    """
    try:
        time = date.split(" ")[1].split(":")
        current_time = datetime.datetime(
            year=1, month=1, day=1, hour=int(time[0]), minute=int(time[1]), second=int(time[2])
        )
        module_logger.info("Определение времени операции")
    except Exception as e:
        module_logger.error(f"Произошла ошибка: {e}")
    else:
        if 4 <= current_time.hour <= 11:
            return "Доброе утро"
        elif 12 <= current_time.hour <= 15:
            return "Добрый день"
        elif 16 <= current_time.hour <= 22:
            return "Добрый вечер"
        else:
            return "Доброй ночи"


def get_cards_info(operations):
    """
    Получение информации о карте, её суммы трат за период времени и кэшбека
    """
    try:
        result = []
        viewed_cards = []
        for operation in operations:
            if operation["card_number"] in viewed_cards:
                continue

            if bool(operation["card_number"]):
                viewed_cards.append(operation["card_number"])
                card_number = operation["card_number"][1:]
            else:
                card_number = None
                viewed_cards.append(card_number)
            spends = [x["payment_amount"] for x in operations if x["card_number"] == operation["card_number"]]
            spends_sum = round(abs(sum(spends)))
            cashback = round(spends_sum / 100, 2)

            card = {"last_digits": card_number, "total_spent": spends_sum, "cashback": cashback}
            result.append(card)
        module_logger.info("Создание информации по картам за период времени")
    except Exception as e:
        module_logger.error(f"Произошла ошибка: {e}")
    else:
        return result


def get_main_payments_categories(operations):
    """
    Получение семи категорий с наибольшими тратами
    """
    try:
        result = []

        all_categories = [x["category"] for x in operations]
        counted = Counter(all_categories).most_common(7)
        categories = [x[0] for x in counted]
        module_logger.info("Создание топ 7 категорий")
        for category in categories:
            amount = sum(
                [abs(x["payment_amount"]) for x in operations if x["category"] == category and x["payment_amount"] < 0]
            )
            data = {"category": category, "amount": int(round(amount))}
            result.append(data)
        module_logger.info("Подсчёт суммы в категориях")
        other_amount = sum(
            [
                abs(x["payment_amount"])
                for x in operations
                if not (x["category"] in categories) and x["payment_amount"] < 0
            ]
        )
        other = {"category": "Остальное", "amount": int(round(other_amount))}
        module_logger.info('Подсчёт категории "Остальное"')
        result.append(other)
    except Exception as e:
        module_logger.error(f"Произошла ошибка: {e}")
    else:
        return result


def get_translations_and_cash(operations):
    """
    Получение суммы переводов и наличных
    """
    try:
        cash = sum(
            [abs(x["payment_amount"]) for x in operations if x["category"] == "Наличные" and x["payment_amount"] < 0]
        )
        module_logger.info("Подсчёт суммы наличных")

        translations = sum(
            [abs(x["payment_amount"]) for x in operations if x["category"] == "Переводы" and x["payment_amount"] < 0]
        )
        module_logger.info("Подсчёт суммы переводов")

        result = [
            {"category": "Наличные", "amount": int(round(cash))},
            {"category": "Переводы", "amount": int(round(translations))},
        ]
    except Exception as e:
        module_logger.error(f"Произошла ошибка: {e}")
    else:
        return result


def get_income(operations):
    """
    Получение суммы прибыли по категориям
    """
    try:
        total_amount = sum([x["payment_amount"] for x in operations if x["payment_amount"] > 0])
        descriptions = []
        result = {"total_amount": int(round(total_amount)), "main": []}
        module_logger.info("Подсчёт всей суммы прибыли")

        for operation in operations:
            if operation["category"] in descriptions:
                continue
            if operation["payment_amount"] > 0:
                category_sum = sum(
                    [
                        x["payment_amount"]
                        for x in operations
                        if x["category"] == operation["category"] and x["payment_amount"] > 0
                    ]
                )
                data = {"category": operation["category"], "amount": int(round(category_sum))}
                result["main"].append(data)
                descriptions.append(operation["category"])
        result["main"].sort(key=lambda x: x["amount"], reverse=True)
        module_logger.info("Подсчёт суммы прибыли по категориям")
    except Exception as e:
        module_logger.error(f"Произошла ошибка: {e}")
    else:
        return result
