#!/usr/bin/env python
# Shebang の設定は利用環境や、コードの規模等で判断して記載。
# 個人的には別になくてもいいと思っているが、
# 前提とするPythonバージョンの説明として、ありかなとも思う。

#---------------------------------
# Python バッチ のテンプレート
# -----
# Python で バッチ処理構築時のテンプレートとして、
# 利用する予定。
# gistから移行。
#---------------------------------

from common import AppParamsd
from common import AppSettings
import common.app_log as app_log

# 終了コード -------
APP_SUCCESS=0	# 成功時
APP_ERROR=1		# エラー終了時

@app_log.entry_log('事前セットアップ')
def setup() -> Settings, AppParams
    
    # アプリケーション設定
    settings = AppSettings()

    # 起動パラメタ
    params = AppParams()

    return settings, params

# 
@app_log.entry_log('Pythonバッチテンプレート')
def main() -> int:
    """エントリーポイント
    終了コードは基本的には、0 or 1。
    TODO: バッチの内容次第で、内容を変えることもあるか？検討が必要。

    Returns:
        int: 終了コード。0:正常終了、1:異常終了
    """    
    
    # 終了コードを初期化
    exit_cod = APP_SUCCESS
    
    # 最上位の例外補足スコープ
    # 小規模でエラーハンドリングが面倒なら、ここでキャッチしてログに吐く。
    # ある程度の規模になり、複数人員で運用する場合は、
    # エラートレースの効率化を目的として、エラーハンドリングのタイミングを検討する。
    try:
        
        # 起動パラメタなどをここで処理
        settings, app_params = setup()

        # ~ 別モジュールに定義された処理を実行 ~ 
        # こんな感じ
        #myproc.execute()
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
    
    # Exceptinでキャッチするので、キャッチ漏れはない。。。はず。
    # 詳細を調べておくこと
    except Exception as e:
        	
        # エラー内容をログに出力
        # > スタックトレースを含めて、例外インスタンスを渡さなくても、
        # > ラッパーが補足して処理してくれてる感じ。たしかloggingモジュールで実装されている。
        # Logger.exception('プログラム名 > hogeデータの作成実行中にエラーが発生しました。')
        
        # 終了コードを「エラー終了」に設定
        exit_code = APP_ERROR    
            	
        return exit_code

# __name__== 'main'で
# サブモジュール時は実行されない。。。はず。
# 一応確認する
if __name__== 'main'
    	
        # sys.exitで終了コードを、コールもとに返す。
    	sys.exit(main())
        