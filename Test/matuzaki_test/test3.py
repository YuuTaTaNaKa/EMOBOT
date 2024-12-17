import tkinter as tk
from PIL import Image, ImageTk  # Pillowライブラリをインポート

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

# デザイン部分を描画する関数（画像を挿入）
def draw_main_screen_design(canvas):
    """メイン画面のデザインを描画"""

    # メッセージ表示
    canvas.create_text(canvas_width / 2, canvas_height / 4, 
                       text="主人公の性別を選んでください。", font=("Arial", 24), fill="black")

    # JPG画像の読み込みと表示
    try:
        # 男性用の画像
        male_img = Image.open("male.jpg")
        male_img = male_img.resize((200, 100))  # サイズを調整
        male_photo = ImageTk.PhotoImage(male_img)
        canvas.create_image(200, 350, image=male_photo, anchor=tk.CENTER)
        canvas.image_male = male_photo  # 参照を保持

        # 女性用の画像
        female_img = Image.open("female.jpg")
        female_img = female_img.resize((200, 100))  # サイズを調整
        female_photo = ImageTk.PhotoImage(female_img)
        canvas.create_image(600, 350, image=female_photo, anchor=tk.CENTER)
        canvas.image_female = female_photo  # 参照を保持
    except Exception as e:
        print("画像の読み込みに失敗しました:", e)

# 画面1: メイン画面
def create_main_screen():
    frame = tk.Frame(root)
    
    # メイン画面用キャンバス
    canvas = tk.Canvas(frame, width=canvas_width, height=canvas_height, bg="lightblue")
    canvas.pack(fill=tk.BOTH, expand=True)

    # デザイン描画（ここを編集で自由に変更可能）
    draw_main_screen_design(canvas)

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

# 画面A: 赤画面
def create_screen_a():
    frame = tk.Frame(root)
    label = tk.Label(frame, text="画面A: 男性", font=("Arial", 24), bg="red", fg="white")
    label.pack(fill=tk.BOTH, expand=True)

    # 戻るボタン
    back_button = tk.Button(frame, text="メイン画面に戻る", command=lambda: switch_frame("main"))
    back_button.pack(pady=20)

    return frame

# 画面B: 緑画面
def create_screen_b():
    frame = tk.Frame(root)
    label = tk.Label(frame, text="画面B: 女性", font=("Arial", 24), bg="green", fg="white")
    label.pack(fill=tk.BOTH, expand=True)

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
