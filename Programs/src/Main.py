from concurrent.futures import ThreadPoolExecutor
import sys
import time
import threading
import InVoice
import Display
import LED

# グローバルで定義された executor 変数と停止フラグ
executor = None
stop_event = threading.Event()  # スレッド停止フラグ

# 各スレッド用のラッパー関数
def run_voice():
    while not stop_event.is_set():
        InVoice.assistant()

def run_display():
    while not stop_event.is_set():
        Display.display()

# メイン処理
def main():
    global executor
    print("スレッドを開始します。")
    # 9つのスレッドで処理を並列実行
    executor = ThreadPoolExecutor(max_workers=9)
    executor.submit(run_voice)
    executor.submit(run_display)
    # executor.submit(LED.led)  # LEDのスレッドも同様に追加

    # プログラムの終了を防ぐために、適宜待機処理を追加
    try:
        while True:
            time.sleep(1)  # 1秒待機
    except KeyboardInterrupt:
        stop()  # Ctrl+Cで停止

# スレッドの終了処理
def stop():
    global executor
    print("スレッドを終了します。")
    stop_event.set()  # 停止フラグをセット
    if executor:
        executor.shutdown(wait=True)  # スレッドが完了するのを待つ
    sys.exit()

# プログラムのエントリーポイント
if __name__ == "__main__":
    main()