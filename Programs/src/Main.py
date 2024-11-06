from concurrent.futures import ThreadPoolExecutor
import sys
import time
import InVoice
import Display
import LED

# グローバルで定義された executor 変数
executor = None

# メイン処理
def main():
    global executor
    print("スレッドを開始します。")
    # 9つのスレッドで処理を並列実行
    executor = ThreadPoolExecutor(max_workers=9)
    executor.submit(InVoice.assistant)
    executor.submit(Display.display)
    # executor.submit(LED.led)

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
    if executor:
        executor.shutdown(wait=True)  # スレッドが完了するのを待つ
    executor.stop()
    sys.exit()

# プログラムのエントリーポイント
if __name__ == "__main__":
    main()