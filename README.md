# Webcam Test

## Installation (python)
```bash 
pip3 install -r requirements
```

## How to run tests
```bash
pytest .  # to run all tests
pytest python_lang/tests/user  # to run only tests from 'user' part
pytest python_lang/tests/user/test_create  # to run only tests from 'user.create/user.get' part
pytest -m positive  # to run only tests with mark 'positive/negative'
```

## API method: user.create

Схема ответа при создании пользователя:
```text
{
    (bool) 'success':
    (dict) 'details:
        (str) 'username':
        (str) 'email':
        (str) 'password':
        (str, date) 'created_at':
        (str, date) 'updated_at':
        (int) 'id':
    (str) 'message':
}
```

Потенциальные проверки:
- Позитивные:
    - создаем нового пользователя с уникальными данными и проверяем, чтобы:
        - success = True
        - message = 'User Successully created'
        - id: больше нуля, прирастает с каждым создаем
        - имя, почта: аналогичные тем, что были указаны в запросе
        - пароль: длинна более 0 символов, не равен по значению тому, что было в запросе
        - даты создания и изменения идентичные друг другу и соответствуют дате отправки запроса (UTC -1)
    - создаем нового пользователя со спецсимволами в:
        - имени
        - почте
        - пароле
- Негативные:
    - создаем пользователя с уже существующими:
        - именем
        - почтой
    - создаем пользователя не заполняя:
        - имя
        - почту
        - пароль
    - создаем пользователя со слишком длинными (надо узнать максимальную длину для каждого поля):
        - именем
        - почтой
        - паролем
    - создаем пользователя со слишком короткими (надо узнать минимальную длину для каждого поля):
        - именем
        - почтой
        - паролей
    - создаем пользователя с почтой, не соответствующей маске электронной почте (проверка на наличие +)

## API method: user.get

Схема ответа при запросе списка пользователей:
```text
[
    {
        (int) 'id':
        (str) 'username':
        (str) 'email':
        (str) 'password':
        (str, date) 'created_at':
        (str, date) 'updated_at':
    },
]
```