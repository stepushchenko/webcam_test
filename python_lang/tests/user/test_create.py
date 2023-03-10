import requests
import time
import pytest
from python_lang import config


class TestUserCreate:
    """
    Схема ответа при создании пользователя:
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

    """

    create_user_positive_test_data = [
        {
            'username': f'user{time.time_ns()}',
            'email': f'user{time.time_ns()}@gmail.com',
            'password': '123',
        },
        {
            'username': f'user😎{time.time_ns()}',
            'email': f'user{time.time_ns()}@gmail.com',
            'password': '123',
        },
    ]

    create_user_negative_test_data = [
        {
            'username': 'user1',
            'email': 'user1@gmail.com',
            'password': '123',
            'message': 'This username is taken. Try another.'
        },
        {
            'username': f'user{time.time_ns()}',
            'email': 'user1@gmail.com',
            'password': '123',
            'message': 'Email already exists'
        },
        {
            'username': '',
            'email': 'user1@gmail.com',
            'password': '123',
            'message': 'A username is required'
        },
        {
            'username': f'user{time.time_ns()}',
            'email': '',
            'password': '123',
            'message': 'An Email is required'
        },
        {
            'username': f'user{time.time_ns()}',
            'email': f'user{time.time_ns()}@gmail.com',
            'password': '',
            'message': 'A password for the user'
        },
    ]  # add other checks

    '''
    Этот тест флакает. Иногда ловится 400 статус код.
    '''
    @pytest.mark.positive
    @pytest.mark.parametrize('test_data', create_user_positive_test_data)
    def test_positive_create_user(self, test_data):
        url = f'{config.url.BASE_URL}/user/create'
        data = {
            'username': test_data['username'],
            'email': test_data['email'],
            'password': test_data['password']
        }
        response = requests.post(url, data=data)
        print(response.json())
        print()
        assert response.status_code == 200
        response = response.json()
        assert response['success'] is True
        assert response['message'] == 'User Successully created'
        assert response['details']['id'] > 0
        assert response['details']['username'] == test_data['username']
        assert response['details']['email'] == test_data['email']
        assert len(response['details']['password']) > 0
        assert response['details']['password'] != test_data['password']
        # add other checks

    @pytest.mark.negative
    @pytest.mark.parametrize('test_data', create_user_negative_test_data)
    def test_negative_create_user(self, test_data):
        url = f'{config.url.BASE_URL}/user/create'
        data = {
            'username': test_data['username'],
            'email': test_data['email'],
            'password': test_data['password']
        }
        response = requests.post(url, data=data)
        print(response.json())
        print()
        assert response.status_code == 400
        response = response.json()
        assert response['success'] is False
        assert response['message'][0] == test_data['message']
