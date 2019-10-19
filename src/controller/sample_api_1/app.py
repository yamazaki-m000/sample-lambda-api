import json
from logging import getLogger

# sys.path.append("/opt")
from config import logger
from config.message import msg as m, Massage
from service import hogehoge_service

logger.set_logger('sample_api_1')
logger = getLogger('sample_api_1')


def lambda_handler_1(event, context):
    param = json.loads(event['body'])
    try:
        error_message, object_context, user_data = hogehoge_service.execute(param)
    except Exception as ex:
        logger.exception(m(Massage.MSG_99_UNEXPECTED_ERROR, ex.__class__.__name__, ex))
        return status500(ex)

    return {
        "statusCode": 200,
        "body": json.dumps({

            "error_message": error_message,
            "object_context_from_s3": object_context,
            "user_data_from_mysql": user_data,
        }),
    }


def lambda_handler_2(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            # "location": ip.text.replace("\n", "")
        }),
    }


def status500(ex: Exception):
    return {
        "statusCode": 500,
        "message": str(ex),
    }
