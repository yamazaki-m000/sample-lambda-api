import os
import sys

# import pdb; pdb.set_trace()

# コマンドラインからpytestを実行した時にソースの方にpathが通るようにする
# ※PyCharm上からだと、srcフォルダの設定で勝手にパス通してくれる

project_root = os.path.abspath(os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + "/../../../"))

sys.path.append(project_root + "/src")
sys.path.append(project_root + "/src/layer/python")
sys.path.append(project_root + "/tests/unit")
