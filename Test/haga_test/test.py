import tkinter as tk
import time
from PIL import Image, ImageTk

# メインウィンドウの作成
root = tk.Tk()
root.title("タッチイベントで画面推移")

"""# ウィンドウの装飾を無効化（タイトルバーを非表示） 
root.overrideredirect(True)"""

# 画面サイズの設定
canvas_width, canvas_height = 960,540 #960,540にて確認
root.geometry(f"{canvas_width}x{canvas_height}")

# 各画面を切り替えるためのフレーム作成
frames = {}

def switch_frame(frame_name):
    """指定されたフレームを表示"""
    for frame in frames.values():
        frame.pack_forget()  # すべてのフレームを非表示
    frames[frame_name].pack(fill=tk.BOTH, expand=True)  # 指定のフレームを表示

    # 時計を更新する関数
def update_clock(canvas, clock_text): 
    current_time = time.strftime("%H:%M") 
    canvas.itemconfig(clock_text, text=current_time) 
    canvas.after(1000, update_clock, canvas, clock_text) # 1秒ごとに更新

# 画面1: メイン画面
def create_main_screen():
    frame = tk.Frame(root)
    
    # メイン画面用キャンバス
    canvas = tk.Canvas(frame, width=canvas_width, height=canvas_height)
    canvas.pack(fill=tk.BOTH, expand=True)
    
    # 画像を読み込み
    image_path = "Test/haga_test/emobot10.jpg"
    img = Image.open(image_path)
    img = img.resize((canvas_width, canvas_height))  # 画像のサイズを調整
    img_tk = ImageTk.PhotoImage(img)
    
    # 画像をキャンバスに表示
    canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
    canvas.image = img_tk  # 画像がガベージコレクションされないように保持
    
    # メッセージ表示
    canvas.create_text(canvas_width / 2, canvas_height / 4, text="主人公の性別を選んでください。", font=("Arial", 24), fill="black")

    # ボタンの領域を描画
    rect1 = canvas.create_rectangle(160, 180, 330, 360, fill="red", outline="black") #左、上、右、下 160, 180, 330, 360にて確認
    canvas.create_text(200, 350, text="男", font=("Arial", 18), fill="white")

    rect2 = canvas.create_rectangle(625, 180, 800, 360, fill="green", outline="black") #左、上、右、下 625, 180, 800, 360にて確認
    canvas.create_text(600, 350, text="女", font=("Arial", 18), fill="white")

    # タッチイベントのバインド
    def on_touch(event):
        if 160 <= event.x <= 180 and 330 <= event.y <= 360: #左、右、上、下
            print("画面Aに移動します")
            switch_frame("screen_a")
        elif 625 <= event.x <= 180 and 800 <= event.y <= 360: #左、右、上、下
            print("画面Bに移動します")
            switch_frame("screen_b")

    canvas.bind("<Button-1>", on_touch)  # 左クリックをタッチとして扱う

    # 時計をキャンバスに追加
    clock_text = canvas.create_text(890, 50, text="", font=("Arial", 24), fill="black") 
    update_clock(canvas, clock_text)

    return frame

# 画面A: 画像Aを表示
def create_screen_a():
    frame = tk.Frame(root)
   
    # 画像を読み込み
    image_path = "Test/haga_test/emobot10.jpg"
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
    image_path = "Test/haga_test/emobot11.jpg"
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

"""# Shiftキーでアプリケーションを終了 
def on_shift(event): 
    if event.keysym == "Shift_L" or event.keysym == "Shift_R": 
        print("アプリケーションを終了します") 
        root.destroy() 
root.bind("<Key>", on_shift)"""

# Escキーでアプリケーションを終了 
def on_esc(event): 
    print("アプリケーションを終了します") 
    root.destroy() 
root.bind("<Escape>", on_esc)

# メインループ
root.mainloop()

#pip install pillow これ入れるかも？