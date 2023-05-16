import json
import structlog
from dm_api_account.models.user_envelope_model import UserRole
from hamcrest import assert_that, has_properties
from services.dm_api_account import Facade

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_put_v1_account_token():
    api = Facade(host='http://localhost:5051')
    response = api.account_api.put_v1_account_token(token='1c627af3-0df1-43da-8d0f-1287b6ad11bb')

    assert_that(response.resource, has_properties(
        {
            "login": "login_18",
            "roles": [UserRole.GUEST, UserRole.PLAYER]
        }

    ))

# expected_json = {'resource': {
#     "login": "login_18",
#     "rating": {
#         "enabled": True,
#         "quality": 0,
#         "quantity": 0
#     },
#      "roles": [
#          "Guest",
#          "Player"
#      ]
#  }}
# actual_json = json.loads(response.json(by_alias=True, exclude_none=True))
# assert actual_json == expected_json
