import utils
import external_api


def home_json_answer(date):
    all_operations = utils.read_excel_file('../data/operations.xlsx')
    user_settings = utils.read_json_file('../user_settings.json')
    operations = utils.get_operations_in_period(all_operations, date)
    cards = utils.get_cards_info(operations)

    sorted_operations = sorted(operations, key=lambda x: x['payment_amount'])
    top_transactions = []
    for operation in sorted_operations[0:5]:
        transaction = {'date': operation['payment_date'],
                       'amount': operation['payment_amount'],
                       'category': operation['category'],
                       'description': operation['description']}
        top_transactions.append(transaction)

    currency_rates = external_api.get_user_currency_rate(user_settings['user_currencies'])
    stock_prices = external_api.get_user_stock_prices(user_settings['user_stocks'])

    result = {'greeting': utils.get_greetings_by_date(date),
              'cards': cards,
              'top_transactions': top_transactions,
              'currency_rates': currency_rates,
              'stock_prices': stock_prices}

    return result

