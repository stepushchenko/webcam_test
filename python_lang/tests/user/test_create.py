import requests
import time
import pytest
from python_lang import config


class TestUserCreate:

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
        assert response.status_code == 400
        response = response.json()
        assert response['success'] is False
        assert response['message'][0] == test_data['message']
