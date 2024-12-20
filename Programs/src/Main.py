import sys
import os
import threading
import time
import InVoice
import Display
# import LED
import Process


def redirect_stderr_to_logfile(logfile="alsa_log.txt"):
    """
    ALSAエラーなど、すべての標準エラー出力を指定されたログファイルにリダイレクトする。
    """
    sys.stderr = open(logfile, 'a')  # 標準エラー出力を追記モードで開く

# メイン処理
def main():
    global threads

    # グローバルスレッドリスト
    threads = []

    # 各機能に対してデーモンスレッドを作成
    voice_thread = threading.Thread(target=Process.assistant, daemon=True)
    # display_thread = threading.Thread(target=Display, daemon=True)
    # led_thread = threading.Thread(target=LED.led, daemon=True)

    # スレッドをリストに追加
    # threads.extend([voice_thread, display_thread])  # led_thread])
    threads.extend([voice_thread])  # led_thread])

    # 標準エラー出力をリダイレクト
    redirect_stderr_to_logfile()

    print("mainスレッドを開始します。")

    # スレッドを開始
    for thread in threads:
        thread.start()

    # プログラムの終了を防ぐために、適宜待機処理を追加
    try:
        while True:
            time.sleep(1)  # 1秒待機
    except KeyboardInterrupt:
        print("\n停止処理を実行します...")
        stop()  # Ctrl+Cで停止


# スレッドの終了処理
def stop():
    print("プログラムを終了します。")
    sys.exit()

# エントリーポイント
if __name__ == "__main__":
    main()