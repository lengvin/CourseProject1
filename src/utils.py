import pandas as pd


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
