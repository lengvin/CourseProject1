from src import views
import re


def main():
    date_format = r'\d\d\d-\d\d-\d\d \d\d:\d\d:\d\d'
    while True:
        print('Информацию с какой страницы вы хотите увидеть, с "Главная" или "События"?')
        user_input = input().lower()
        if user_input == 'главная':
            while True:
                print('Введите дату в формате ГГГГ-ММ-ДД ЧЧ:ММ:СС по которую вы хотите увидеть информацию')
                user_input = input().lower()
                if bool(re.search(date_format, user_input, flags=re.IGNORECASE)):
                    result = views.home_json_answer(user_input)
                    print(result)
                    break
                else:
                    print('некоректный ввод, повторите попытку')
            break
        elif user_input == 'события':
            while True:
                print('Введите дату в формате ГГГГ-ММ-ДД ЧЧ:ММ:СС по которую вы хотите увидеть информацию')
                user_input = input().lower()
                date = user_input
                if bool(re.search(date_format, user_input, flags=re.IGNORECASE)):
                    print('Введите промежуток времени, за ктоторый были произведены операции \n'
                          'W - неделя \n'
                          'M - месяц \n'
                          'Y - год \n'
                          'ALL - все операции до указанной даты')
                    user_input = input().upper()
                    if user_input in ['W', 'M', 'Y', 'ALL']:
                        result = views.events_json_answer(date, period=user_input)
                        print(result)
                        break
                    else:
                        print('некоректный ввод, повторите попытку')
                else:
                    print('некоректный ввод, повторите попытку')
            break
        else:
            print('Некоректный ввод, повторите попытку')


if __name__ == '__main__':
    main()
