# プログラムの起動・終了、スレッドの管理・作成・実行
# モジュール・プログラムファイルのインポート
from concurrent.futures import ThreadPoolExecutor
import sys
import time
import InVoice
import InIR
import Display
import LED

# 処理の記述
def main():
    print("スレッドを開始します。")
    executor = ThreadPoolExecutor(max_workers=9)
    executor.submit(InVoice.assistant)
    executor.submit(InIR.inputIR)
    executor.submit(Display.display)
    executor.submit(LED.led)
        
if __name__ == "__main__":
    main()

def stop():
        print("スレッドを終了します。")
        sys.exit()