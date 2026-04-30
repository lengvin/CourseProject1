from src import api_processing, aeroplanes_logic, files_processing
from src.utils import user_choice, choice_criterion, choice_exist_file_path, choice_top_n, user_output


def user_interface():
    while True:
        try:
            print('Введите название страны')
            country = input().title()
            api = api_processing.GetAeroplanes()
            all_aeroplanes = api.get_aeroplanes(country)['states']
            all_aeroplanes_obj_list = aeroplanes_logic.Aeroplane.cast_to_object_list(all_aeroplanes)
        except IndexError:
            print('Некорректное название страны, повторите попытку')
        else:
            if user_choice('Хотите указать свой путь к json-файлу для сохранения в нём каталога самолётов выбранной страны?'):
                file_path = choice_exist_file_path()
                user_json_saver = files_processing.JSONSaver(file_path)
            else:
                user_json_saver = files_processing.JSONSaver()

            for obj in all_aeroplanes_obj_list:
                user_json_saver.add_aeroplane(obj)

            if user_choice('Отфильтровать самолёты по одному определённому критерию?'):
                user_criterion, user_value = choice_criterion()
                user_list = user_json_saver.get_by_criterion_from_json(user_criterion, user_value)
            else:
                user_list = user_json_saver.get_json_data()

            if user_choice('Вывести топ N самолётов по высоте?'):
                while True:
                    try:
                        user_top = choice_top_n(len(user_list))
                        user_list = user_json_saver.get_top_by_height(user_list, user_top)
                    except ValueError:
                        print('Введённое вами число самолётов превышает число имеющихся самолётов, повторите попытку')
                    else:
                        break

            user_output(user_list)
            break


if __name__ == '__main__':
    user_interface()
