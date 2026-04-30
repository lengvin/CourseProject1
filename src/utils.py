import os
from typing import Union


def user_choice(question):
    while True:
        print(question)
        user_input = input().lower()
        if user_input == "да":
            return True
        elif user_input == "нет":
            return False
        else:
            print("Некорректный ввод ответа, повторите попытку")


def choice_criterion():
    while True:
        print(
            "Введите один из следующих критериев: \n"
            "страна регистрации, позывной, горизонтальная скорость, вертикальная скорость, геометрическая высота"
        )
        user_criteria = input().lower()

        if user_criteria in [
            "страна регистрации",
            "позывной",
            "горизонтальная скорость",
            "вертикальная скорость",
            "геометрическая высота",
        ]:
            criteria_dict = {
                "страна регистрации": "country",
                "позывной": "callsign",
                "горизонтальная скорость": "velocity",
                "вертикальная скорость": "vertical_rate",
                "геометрическая высота": "geo_altitude",
            }
            criterion = criteria_dict[user_criteria]
            break
        else:
            print("Некорректный ввод, повторите попытку")
    while True:
        print("Введите значение выбранного вами критерия")
        value = input()
        if criterion in ["country", "callsign"]:
            if isinstance(value, str):
                return criterion, value
            else:
                print("Некорректный ввод, повторите попытку")
        elif criterion in ["velocity", "vertical_rate", "geo_altitude"]:
            try:
                if value == "None":
                    return criterion, None
                elif bool(float(value)):
                    return criterion, float(value)
                elif int(value) == 0:
                    return criterion, int(value)
            except ValueError:
                print("Некорректный ввод, повторите попытку")


def choice_exist_file_path():
    while True:
        print("Введите путь к файлу для сохранения в нём всех самолётов выбранной страны в формате json")
        user_input = input()
        if os.path.exists(user_input):
            return user_input
        else:
            print("указанного файла не существует, повторите попытку, введя существующий файл:")


def choice_top_n(len_of_data):
    while True:
        print(f"Введите топ-n самолётов по высоте (всего {len_of_data} самолётов)")
        user_input = input()
        if user_input.isdigit():
            return int(user_input)
        else:
            print("Некорректный ввод, повторите попытку")


def user_output(data):
    for aeroplane in data:
        print(
            f'Страна регистрации:{aeroplane["country"]}; Позывной:{aeroplane["callsign"]}; Горизонтальная скорость:{aeroplane["velocity"]}; Вертикальная скорость:{aeroplane["vertical_rate"]}; Геометрическая высота:{aeroplane["geo_altitude"]} \n'
        )
