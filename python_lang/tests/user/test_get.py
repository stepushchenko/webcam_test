import requests
import time
import pytest
from python_lang import config


class TestUserGet:

    def test_user_get(self):
        url = f'{config.url.BASE_URL}/user/get'
        response = requests.get(url)
        assert response.status_code == 200
