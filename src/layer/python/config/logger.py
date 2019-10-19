# ログのライブラリ
import logging
import os
from logging import getLogger, StreamHandler, Formatter

# TODO: 下記のパラメータを環境変数で管理する
log_format = os.environ['LOG_FORMAT'].replace('\\t', '\t')
log_level = os.environ['LOG_LEVEL']
log_level = logging.getLevelName(log_level)


# ログの出方を全力にする（boto3とかが出力するログも全部出す）
# root_logger = getLogger()
# root_logger.setLevel(config.DEBUG)
# if len(root_logger.handlers) == 0:
#     h = StreamHandler()
#     h.setFormatter(Formatter(fmt=log_format))
#     root_logger.addHandler(h)

def set_logger(name: str):
    # loggerオブジェクトの宣言
    logger = getLogger(name)

    # loggerのログレベル設定(ハンドラに渡すエラーメッセージのレベル)
    logger.setLevel(log_level)

    # 以降の処理はハンドラが設定されてない時だけ
    # メソッドコールされる度に↓をやっていると、ログがどんどん多重になっていく
    if len(logger.handlers) == 0:
        # handlerの生成
        stream_handler = StreamHandler()

        # handlerのログレベル設定(ハンドラが出力するエラーメッセージのレベル)
        stream_handler.setLevel(log_level)

        # ログ出力フォーマット設定
        handler_format = Formatter(log_format)
        stream_handler.setFormatter(handler_format)

        logger.addHandler(stream_handler)
        logger.propagate = False
