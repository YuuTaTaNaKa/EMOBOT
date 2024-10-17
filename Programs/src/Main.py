# プログラムの起動・終了、スレッドの管理・作成・実行
# モジュール・プログラムファイルのインポート
import threading
import time
import InVoice
import InIR
import BatteryMonitor
import Display

# 処理の記述
def main():
    print("メイン関数の実行")
    # スレッドの作成
    battery = threading.Thread(target=BatteryMonitor.battery,name="battery",demon=True)
    voice = threading.Thread(target=InVoice.voice,name="voice",demon=True)
    display = threading.Thread(target=Display.display,name="display",demon=True)
    ir = threading.Thread(target=InIR.InputIR,name="ir",demon=True)
    # スレッドの開始

if __name__ == "__main__":
    main()