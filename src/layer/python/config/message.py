"""
ログメッセージ
"""

from enum import Enum, unique


@unique
class Massage(Enum):
    MSG_01_INFO_RUNNING_REQUEST = 'AP1001I'
    MSG_01_INFO_RUNNING_RESPONSE = 'AP1002I'

    MSG_99_UNEXPECTED_ERROR = 'AP9999E'


messages_format = {
    Massage.MSG_01_INFO_RUNNING_REQUEST.value: '[%MSG_CODE%] request: {}',
    Massage.MSG_01_INFO_RUNNING_RESPONSE.value: '[%MSG_CODE%] response: {}',

    Massage.MSG_99_UNEXPECTED_ERROR.value: '[%MSG_CODE%] unexpected error {} {}'
}


def msg(massage, *args):
    msg = messages_format[massage.value]

    if "%MSG_CODE%" in msg:
        msg = msg.replace('%MSG_CODE%', massage.value)

    return msg.format(*args)
