import requests
import json
from services.dm_api_account import Facade


def test_post_v1_account_password():
    api = Facade(host='http://localhost:5051')
    json = {
        "login": "login_1",
        "email": "asd@gmail.com"
    }
    response = api.account_api.post_v1_account_password(
        json=json
    )

    print(response)
