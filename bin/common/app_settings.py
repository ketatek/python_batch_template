#-----------------------------------------
# バッチアプリの設定 の アクセッサなどを実装
# Python 3.11 でtoml パーサーが提供されるようになったため、
# tomlを前提とすることにした。
#-----------------------------------------
import tomllib
from pprint import pprint
import utils

class AppSettings():
"""
# 設定ファイル(toml)の取扱クラス

issue:  
* portableな構成を前提に、以下のパスがデフォルトとしたい。  
    <メインモジュール配置先>/config/settings.toml
* ファイルの有無による動作を定義できるようにしたい。
    * ファイルなしを許容するなら、デフォルト値を定義
    * ファイルなしを許容しないなら、その場で例外スロー
* globalな設定を前提とするため、singltonな形式で提供したい。
* validaterの実装が必要。
"""
    

    def get_settings_path(path: str) -> str:
        
        ret = str(utils.get_root_path() / 'config' / 'settings.toml')

        if path is not None:
            ret = path

        return ret

    def load_settings(path: str):
        
        path = get_settings_path(path)

        with open(path, mode="rb") as f:
            tomllib.load(f)
