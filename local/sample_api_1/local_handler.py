# SAMでやりたいことが出来ない人が頑張ってローカルで実行するためのスクリプト
import json

from controller.sample_api_1 import app


def lambda_handler(apigw_event):
    ret = app.lambda_handler_1(apigw_event, "")
    print(json.dumps(ret))


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


if __name__ == "__main__":
    # ローカルからテストする時は、このスクリプトをpython的に実行させる
    # ※SAMが使えない人向け（使えるけどデバッガで停止できない場合とかも）
    import sys
    import os

    os.chdir(f"{__file__}/../../../src")

    # pythonのパス通すための位置調整
    # ※{project_home}の中にあるディレクトリにパスを通す
    target = [
        f'{os.getcwd()}',
        # f'{os.getcwd()}\\..\\tests\\unit',
        f'{os.getcwd()}\\layer\\python'
    ]
    sys.path.extend(target)

    lambda_handler(data())
