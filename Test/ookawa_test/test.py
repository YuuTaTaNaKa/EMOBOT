import tkinter as tk
from PIL import Image, ImageTk

# メインウィンドウの作成
root = tk.Tk()
root.title("タッチイベントで画面推移")

# 画面サイズの設定
canvas_width, canvas_height = 800, 600
root.geometry(f"{canvas_width}x{canvas_height}")

# 各画面を切り替えるためのフレーム作成
frames = {}

def switch_frame(frame_name):
    """指定されたフレームを表示"""
    for frame in frames.values():
        frame.pack_forget()  # すべてのフレームを非表示
    frames[frame_name].pack(fill=tk.BOTH, expand=True)  # 指定のフレームを表示

# 画面1: メイン画面
def create_main_screen():
    frame = tk.Frame(root)
    
    # メイン画面用キャンバス
    canvas = tk.Canvas(frame, width=canvas_width, height=canvas_height)
    canvas.pack(fill=tk.BOTH, expand=True)
    
    # 画像を読み込み
    image_path = "Test/ookawa_test/emobot1.jpg"
    img = Image.open(image_path)
    img = img.resize((canvas_width, canvas_height))  # 画像のサイズを調整
    img_tk = ImageTk.PhotoImage(img)
    
    # 画像をキャンバスに表示
    canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
    canvas.image = img_tk  # 画像がガベージコレクションされないように保持
    
    # メッセージ表示
    canvas.create_text(canvas_width / 2, canvas_height / 4, text="主人公の性別を選んでください。", font=("Arial", 24), fill="black")

    # ボタンの領域を描画
    """rect1 = canvas.create_rectangle(100, 300, 300, 400, fill="red", outline="black")
    canvas.create_text(200, 350, text="男", font=("Arial", 18), fill="white")

    rect2 = canvas.create_rectangle(500, 300, 700, 400, fill="green", outline="black")
    canvas.create_text(600, 350, text="女", font=("Arial", 18), fill="white")"""

    # タッチイベントのバインド
    def on_touch(event):
        if 100 <= event.x <= 300 and 300 <= event.y <= 400:
            print("画面Aに移動します")
            switch_frame("screen_a")
        elif 500 <= event.x <= 700 and 300 <= event.y <= 400:
            print("画面Bに移動します")
            switch_frame("screen_b")

    canvas.bind("<Button-1>", on_touch)  # 左クリックをタッチとして扱う

    return frame

# 画面A: 画像Aを表示
def create_screen_a():
    frame = tk.Frame(root)
    
    # 画像を読み込み
    image_path = "Test/ookawa_test/emobot1.jpg"
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
def create_screen_b():
    frame = tk.Frame(root)
    
    # 画像を読み込み
    image_path = "Test/ookawa_test/emobot2.jpg"
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

# フレームを登録
frames["main"] = create_main_screen()
frames["screen_a"] = create_screen_a()
frames["screen_b"] = create_screen_b()

# 最初の画面を表示
switch_frame("main")

# メインループ
root.mainloop()