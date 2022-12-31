import argparse

class AppParams():
  """
  # 起動パラメタの取扱クラス
  __init__ で argparseを利用して、アプリケーションの起動パラメタを読込み検証。  
  プロパティで読込んだパラメタにアクセスできるよう実装している。  
  dictを継承すれば、この実装自体必要ないかもしれないが、
  エディタのオートコンプリートが動作しないため、この実装が妥当か？要調査。
  """
  
  __params = {}
  """
  パラメタ格納先
  """
  
  @property
  param_a(self) -> str:
    return self.__params.param_a
   
  def __init__(self) -> None:
    parser = argparse.ArgumentParser(prog="プログラム名")
    
    parser.add_argument('params_a', type=str, help=’パラメタ説明’)
    
    self.__params = parser.parse_args()