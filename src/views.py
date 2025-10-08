from src import external_api
from src import utils


def home_json_answer(date):
    """
    Создание JSON ответа для страницы "главная"
    """
    all_operations = utils.read_excel_file("data/operations.xlsx")
    user_settings = utils.read_json_file("user_settings.json")
    operations = utils.get_operations_in_period(all_operations, date, "M")
    cards = utils.get_cards_info(operations)

    sorted_operations = sorted(operations, key=lambda x: x["payment_amount"])
    top_transactions = []
    for operation in sorted_operations[0:5]:
        transaction = {
            "date": operation["payment_date"],
            "amount": operation["payment_amount"],
            "category": operation["category"],
            "description": operation["description"],
        }
        top_transactions.append(transaction)

    currency_rates = external_api.get_user_currency_rate(user_settings["user_currencies"])
    stock_prices = external_api.get_user_stock_prices(user_settings["user_stocks"])

    result = {
        "greeting": utils.get_greetings_by_date(date),
        "cards": cards,
        "top_transactions": top_transactions,
        "currency_rates": currency_rates,
        "stock_prices": stock_prices,
    }

    return result


def events_json_answer(date, period="M"):
    """
    Создание JSON ответа для страницы "события"
    """
    all_operations = utils.read_excel_file("data/operations.xlsx")
    user_settings = utils.read_json_file("user_settings.json")

    operations = utils.get_operations_in_period(all_operations, date, period=period)
    total_amount = sum([abs(x["payment_amount"]) for x in operations if x["payment_amount"] < 0])
    main_spends = utils.get_main_payments_categories(operations)
    transfers_and_cash = utils.get_translations_and_cash(operations)
    income = utils.get_income(operations)

    currency_rates = external_api.get_user_currency_rate(user_settings["user_currencies"])
    stock_prices = external_api.get_user_stock_prices(user_settings["user_stocks"])

    result = {
        "expenses": {"total_amount": int(round(total_amount)), "main": main_spends},
        "transfers_and_cash": transfers_and_cash,
        "income": income,
        "currency_rates": currency_rates,
        "stock_prices": stock_prices,
    }

    return result
