import json
import os
from logging import getLogger

import boto3
import dataset
from cerberus import Validator

from config.message import msg as m, Massage

logger = getLogger('sample_api_1')


def execute(params: dict):
    logger.info(m(Massage.MSG_01_INFO_RUNNING_REQUEST, json.dumps(params)))
    error_message = validate(params)
    object_context = get_object_from_s3()
    user_data = get_user_data_from_mysql('TOM')
    return error_message, object_context, user_data


def validate(params: dict):
    # Cerberusサンプル
    v = Validator({'test': {'type': 'string'}})
    v.validate(params)
    return v.errors


def get_object_from_s3():
    # S3アクセスサンプル
    s3_client = boto3.client("s3", endpoint_url=os.getenv('S3_ENDPOINT', None))
    response = s3_client.get_object(Bucket=os.environ['S3_BUCKET'], Key='template.txt')
    body = response['Body'].read()
    context = body.decode('utf-8')
    return context


def get_user_data_from_mysql(user_name: str):
    db = dataset.connect(os.environ['DB_ENDPOINT'])
    user_table = db['users']
    results = user_table.find_one(name=user_name)
    # TODO: datasetのデフォルトの設定により、この時点でコネクションが2つ繋がる。　Appの構造上、コネクションは1つで良いので、コネクションを1つになるように実装する。
    # →これで現在のコネクションを確認できる。　SHOW STATUS like 'Threads_connected';
    return results
