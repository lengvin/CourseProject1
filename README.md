# Приложение для анализа банковских операций

## Описание:

Приложение для анализа банковских операций - это приложение, которое генерирует JSON-данные для веб-страниц.

## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/lengvin/CourseProject1.git
```

## Тестирование

Все модули покрыты тестами на 80%


## Модуль views.py

### Функция home_json_answer

Функция создаёт JSON-ответ для страницы "Главная", пример использования:
```
from views import home_json_answer

home_json_answer(date)
```

### Функция events_json_answer

Функция создаёт JSON-ответ для страницы "События", пример использования:
```
from views import events_json_answer

events_json_answer(date, period=period)
```
