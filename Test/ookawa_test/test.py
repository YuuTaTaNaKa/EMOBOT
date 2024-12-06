import tkinter as tk
from PIL import Image, ImageTk

# メインウィンドウの作成
root = tk.Tk()
root.title("タッチイベントで画面推移")

# ウィンドウの装飾を無効化（タイトルバーを非表示） 
#root.overrideredirect(True)

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
    #rect1 = canvas.create_rectangle(160, 180, 330, 360, fill="red", outline="black") #左、上、右、下 160, 180, 330, 360にて確認
    canvas.create_text(245, 290, text="男", font=("Arial", 30), fill="black")

    #rect2 = canvas.create_rectangle(625, 180, 800, 360, fill="green", outline="black") #左、上、右、下 625, 180, 800, 360にて確認
    canvas.create_text(710, 290, text="女", font=("Arial", 30), fill="black")

    # タッチイベントのバインド
    def on_touch(event):
        if 160 <= event.x <= 330 and 180 <= event.y <= 360: #左、右、上、下
            print("画面Aに移動します")
            switch_frame("screen_a")
        elif 625 <= event.x <= 800 and 180 <= event.y <= 360: #左、右、上、下
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
    canvas.create_text(245, 290, text="戻る", font=("Arial", 30), fill="black") 
    def on_touch(event): 
        if 160 <= event.x <= 330 and 180 <= event.y <= 360: # 左、右、上、下 
            print("メイン画面に戻ります") 
            switch_frame("main") 

    canvas.bind("<Button-1>", on_touch) # 左クリックをタッチとして扱う
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
    canvas.create_text(245, 290, text="戻る", font=("Arial", 30), fill="black")
    
    # タッチイベントのバインド 
    def on_touch(event): 
        if 160 <= event.x <= 330 and 180 <= event.y <= 360: # 左、右、上、下 
            print("メイン画面に戻ります")
            
            switch_frame("main") 

    canvas.bind("<Button-1>", on_touch) # 左クリックをタッチとして扱う
    

    return frame

# フレームを登録
frames["main"] = create_main_screen()
frames["screen_a"] = create_screen_a()
frames["screen_b"] = create_screen_b()

# 最初の画面を表示
switch_frame("main")

# メインループ
root.mainloop()

#pip install pillow これ入れるかも？