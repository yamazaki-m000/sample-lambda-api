import json
from http import HTTPStatus

from controller.sample_api_1 import app


class TestCase:
    def test_正常系_sample(self):
        ret = app.lambda_handler_1(data(), "")
        print(ret)
        asserts_normal(ret)


def asserts_normal(ret):
    """
    正常系assertion
    """

    # HTTPステータス確認
    assert ret['statusCode'] == HTTPStatus.OK
    body = ret['body']
    body = json.loads(body)

    # レスポンスの期待値
    expected_body = {"error_message": {}, "object_context_from_s3": "testtesttesttest",
                     "user_data_from_mysql": {"id": 1, "name": "TOM", "email": "xxxx@mail.co.jp"}}

    # レスポンスの中身の確認
    assert body == expected_body


def data():
    """
    APIGatewayからLambdaに渡されるHTTPのデータのテスト用ダミーを返す

    Returns
    -------
    return_data: テスト用のJSONデータ

    """

    test = 'body'

    body = f'{{ "test": "{test}"}}'

    return {
        "body": body,
        "headers": {
            "User-Agent": "Custom User Agent String",
        },
    }
