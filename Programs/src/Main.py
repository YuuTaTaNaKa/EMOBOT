import threading
import sys
import time
import InVoice
import Display
import LED
import Process

# グローバルで定義されたスレッドリスト
threads = []

# メイン処理
def main():
    global threads
    print("スレッドを開始します。")
    
    # 各機能に対してデーモンスレッドを作成
    voice_thread = threading.Thread(target=Process.assistant, daemon=True)
    display_thread = threading.Thread(target=Display.display, daemon=True)
    # led_thread = threading.Thread(target=LED.led, daemon=True)
    
    # スレッドをリストに追加
    threads.extend([voice_thread, display_thread]) # led_thread])

    # スレッドを開始
    for thread in threads:
        thread.start()

    # プログラムの終了を防ぐために、適宜待機処理を追加
    print ("test")
    try:
        while True:
            time.sleep(1)  # 1秒待機
    except KeyboardInterrupt as e:
        print(e)
        stop()  # Ctrl+Cで停止

# スレッドの終了処理
def stop():
    print("プログラムを終了します。")
    sys.exit()

# プログラムのエントリーポイント
if __name__ == "__main__":
    main()