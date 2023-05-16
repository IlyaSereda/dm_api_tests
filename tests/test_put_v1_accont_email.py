import requests
import json

from services.dm_api_account import Facade


def test_put_v1_account_email():
    api = Facade(host='http://localhost:5051')
    json = {
        "login": "login_1",
        "password": "Login_11",
        "email": "asdasd@gmail.com"
    }
    response = api.account_api.put_v1_account_email(
        json=json
    )

    print(response)
