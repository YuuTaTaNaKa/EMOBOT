import threading
import sys
import time
import os
import InVoice
import Display
import LED
from contextlib import redirect_stderr

# グローバルで定義されたスレッドリスト
threads = []

# エラー出力を/dev/nullにリダイレクトするコンテキスト
class NullError:
    def __enter__(self):
        self.devnull = open(os.devnull, 'w')
        self.original_stderr = sys.stderr
        sys.stderr = self.devnull
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stderr = self.original_stderr
        self.devnull.close()

# メイン処理
def main():
    global threads
    print("スレッドを開始します。")

    # 各機能に対してデーモンスレッドを作成
    voice_thread = threading.Thread(target=run_in_silence, args=(InVoice.assistant,), daemon=True)
    display_thread = threading.Thread(target=Display.display, daemon=True)
    # led_thread = threading.Thread(target=LED.led, daemon=True)

    # スレッドをリストに追加
    threads.extend([voice_thread, display_thread])  # led_thread])

    # スレッドを開始
    for thread in threads:
        thread.start()

    # プログラムの終了を防ぐために、適宜待機処理を追加
    try:
        while True:
            time.sleep(1)  # 1秒待機
    except KeyboardInterrupt as e:
        print("\n停止処理を実行します...")
        stop()  # Ctrl+Cで停止

# 特定の処理をエラー出力を無効化した状態で実行
def run_in_silence(target_function):
    """
    指定された関数をエラー出力を/dev/nullにリダイレクトした状態で実行する。
    """
    with NullError():
        target_function()

# スレッドの終了処理
def stop():
    print("プログラムを終了します。")
    sys.exit()

# プログラムのエントリーポイント
if __name__ == "__main__":
    main()
