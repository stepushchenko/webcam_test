import requests
import time
import pytest
from python_lang import config


class TestUserGet:
    """
    Схема ответа при запросе списка пользователей:
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
    """

    def test_user_get(self):
        url = f'{config.url.BASE_URL}/user/get'
        response = requests.get(url)
        print(response.json())
        print()
        assert response.status_code == 200
