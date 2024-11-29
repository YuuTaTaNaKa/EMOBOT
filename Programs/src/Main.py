import sys
import os
import threading
import time
import InVoice
# import Display
import LED
import time
import tkinter
import tkinter as tk
from PIL import Image, ImageTk


# グローバルスレッドリスト
threads = []
# 各画面を切り替えるためのフレーム作成
frames = {}

def redirect_stderr_to_logfile(logfile="alsa_log.txt"):
    """
    ALSAエラーなど、すべての標準エラー出力を指定されたログファイルにリダイレクトする。
    """
    sys.stderr = open(logfile, 'a')  # 標準エラー出力を追記モードで開く

# メイン処理
def main():
    global threads

    # 標準エラー出力をリダイレクト
    redirect_stderr_to_logfile()

    print("スレッドを開始します。")

    # 各機能に対してデーモンスレッドを作成
    voice_thread = threading.Thread(target=InVoice.assistant, daemon=True)
    display_thread = threading.Thread(target=Display.display, daemon=True)
    # led_thread = threading.Thread(target=LED.led, daemon=True)

    # スレッドをリストに追加
    threads.extend([voice_thread, display_thread])  # led_thread])
    # threads.extend([voice_thread])  # led_thread])

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

def Display():
    # メインウィンドウの作成
    root = tk.Tk()
    root.title("タッチイベントで画面推移")

    # 画面サイズの設定
    canvas_width, canvas_height = 800, 600
    root.geometry(f"{canvas_width}x{canvas_height}")

def switch_frame(frame_name):
    """指定されたフレームを表示"""
    for frame in frames.values():
        frame.pack_forget()  # すべてのフレームを非表示
    frames[frame_name].pack(fill=tk.BOTH, expand=True)  # 指定のフレームを表示

    # 画面1: メイン画面
def create_main_screen(root, canvas_width, canvas_height):
    frame = tk.Frame(root)
    
    # メイン画面用キャンバス
    canvas = tk.Canvas(frame, width=canvas_width, height=canvas_height)
    canvas.pack(fill=tk.BOTH, expand=True)
    
    # 画像を読み込み
    image_path = "Programs\img\emobot1.jpg"
    img = Image.open(image_path)
    img = img.resize((canvas_width, canvas_height))  # 画像のサイズを調整
    img_tk = ImageTk.PhotoImage(img)
    
    # 画像をキャンバスに表示
    canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
    canvas.image = img_tk  # 画像がガベージコレクションされないように保持
    
    # メッセージ表示
    # canvas.create_text(canvas_width / 2, canvas_height / 4, text="主人公の性別を選んでください。", font=("Arial", 24), fill="black")

    # ボタンの領域を描画
    """rect1 = canvas.create_rectangle(100, 300, 300, 400, fill="red", outline="black")
    canvas.create_text(200, 350, text="男", font=("Arial", 18), fill="white")

    rect2 = canvas.create_rectangle(500, 300, 700, 400, fill="green", outline="black")
    canvas.create_text(600, 350, text="女", font=("Arial", 18), fill="white")"""
    
    canvas.bind("<Button-1>", on_touch)  # 左クリックをタッチとして扱う

    return frame

    # タッチイベントのバインド
def on_touch(event):
    if 100 <= event.x <= 300 and 300 <= event.y <= 400:
        print("画面Aに移動します")
        switch_frame("screen_a")
    elif 500 <= event.x <= 700 and 300 <= event.y <= 400:
        print("画面Bに移動します")
        switch_frame("screen_b")


# 画面A: 画像Aを表示
def create_screen_a(root, canvas_width, canvas_height):
    frame = tk.Frame(root)
    
    # 画像を読み込み
    image_path = "Programs\img\emobot1.jpg"
    img = Image.open(image_path)
    img = img.resize((canvas_width, canvas_height))  # 画像のサイズを調整
    img_tk = ImageTk.PhotoImage(img)
    
    # 画像をキャンバスに表示
    canvas = tk.Canvas(frame, width=canvas_width, height=canvas_height)
    canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
    canvas.image = img_tk  # 画像がガベージコレクションされないように保持
    canvas.pack(fill=tk.BOTH, expand=True)
    
    # 戻るボタン
    back_button = tk.Button(frame, text="メイン画面に戻る", command=lambda: switch_frame("main"))
    back_button.pack(pady=20)

    return frame

# 画面B: 画像Bを表示
def create_screen_b(root, canvas_width, canvas_height):
    frame = tk.Frame(root)
    
    # 画像を読み込み
    image_path = "Programs\img\emobot2.jpg"
    img = Image.open(image_path)
    img = img.resize((canvas_width, canvas_height))  # 画像のサイズを調整
    img_tk = ImageTk.PhotoImage(img)
    
    # 画像をキャンバスに表示
    canvas = tk.Canvas(frame, width=canvas_width, height=canvas_height)
    canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
    canvas.image = img_tk  # 画像がガベージコレクションされないように保持
    canvas.pack(fill=tk.BOTH, expand=True)
    
    # 戻るボタン
    back_button = tk.Button(frame, text="やり直す", command=lambda: switch_frame("main"))
    back_button.pack(pady=20)

    return frame


# スレッドの終了処理
def stop():
    print("プログラムを終了します。")
    sys.exit()

# エントリーポイント
if __name__ == "__main__":
    main()
