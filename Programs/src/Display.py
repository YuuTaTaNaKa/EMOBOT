import pygame
import os
import sys
# from gpiozero import LED, Button
# from signal import pause

try:
    #pathの読み込み
    base_path = os.path.join("Programs","img")

    # boy画像
    boy_Default_image = pygame.image.load(os.path.join(base_path, "boy_Default.jpg"))
    boy_smile_image = pygame.image.load(os.path.join(base_path, "boy_smile.jpg"))
    boy_kirarin_image = pygame.image.load(os.path.join(base_path, "boy_kirarin.jpg"))
    boy_anger_image = pygame.image.load(os.path.join(base_path, "boy_anger.jpg"))
    boy_doubt_image = pygame.image.load(os.path.join(base_path, "boy_doubt.jpg"))
    boy_embarrassed_image = pygame.image.load(os.path.join(base_path, "boy_embarrassed.jpg"))
    boy_thinEye_image = pygame.image.load(os.path.join(base_path, "boy_thinEye.jpg"))
    boy_wink_image = pygame.image.load(os.path.join(base_path, "boy_wink.jpg"))
    boy_sleep_image = pygame.image.load(os.path.join(base_path, "boy_sleep.jpg"))
    boy_sad_image = pygame.image.load(os.path.join(base_path, "boy_sad.jpg"))
    boy_omg_image = pygame.image.load(os.path.join(base_path, "boy_omg.jpg"))
    # girl画像
    girl_Default_image = pygame.image.load(os.path.join(base_path, "girl_Default.jpg"))
    girl_smile_image = pygame.image.load(os.path.join(base_path, "girl_smile.jpg"))
    girl_kirarin_image = pygame.image.load(os.path.join(base_path, "girl_kirarin.jpg"))
    girl_anger_image = pygame.image.load(os.path.join(base_path, "girl_anger.jpg"))
    girl_doubt_image = pygame.image.load(os.path.join(base_path, "girl_doubt.jpg"))
    girl_embarrassed_image = pygame.image.load(os.path.join(base_path, "girl_embarrassed.jpg"))
    girl_thinEye_image = pygame.image.load(os.path.join(base_path, "girl_thinEye.jpg"))
    girl_wink_image = pygame.image.load(os.path.join(base_path, "girl_wink.jpg"))
    girl_sleep_image = pygame.image.load(os.path.join(base_path, "girl_sleep.jpg"))
    girl_sad_image = pygame.image.load(os.path.join(base_path, "girl_sad.jpg"))
    girl_omg_image = pygame.image.load(os.path.join(base_path, "girl_omg.jpg"))

    # 現在の画像
    current_boy_image = boy_Default_image
    current_girl_image = girl_Default_image

except pygame.error as e:
    print(f"画像の読み込みエラー: {e}")
    # LED.led_error()
    pygame.quit()
    # sys.exit()

def resize_image(image, screen_width, screen_height):
    """画像をフルスクリーンに合わせてリサイズする"""
    img_width, img_height = image.get_width(), image.get_height()
    aspect_ratio = img_width / img_height
    if screen_width / screen_height > aspect_ratio:
        new_width = int(screen_height * aspect_ratio)
        new_height = screen_height
    else:
        new_width = screen_width
        new_height = int(screen_width / aspect_ratio)
    return pygame.transform.scale(image, (new_width, new_height))

def display():
    # Pygameの初期化
    pygame.init()

    # 色の定義 (RGB形式)
    WHITE = (255, 255, 255)

    # 画像の初期表示
    current_screen = "boy"

    # フルスクリーンの解像度を取得
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  # フルスクリーンの設定
    screen_width, screen_height = screen.get_size()

    # スワイプに関連する変数
    is_swiping = False
    start_pos = None
    end_pos = None
    swipe_threshold = 50  # スワイプと判定する最低距離

    # メインループ
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # ESCキーが押されたら終了
                    running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                is_swiping = True
                start_pos = event.pos
            elif event.type == pygame.MOUSEBUTTONUP:
                is_swiping = False
                end_pos = event.pos

                if start_pos and end_pos:
                    # スワイプ方向を計算
                    dx = end_pos[0] - start_pos[0]
                    dy = end_pos[1] - start_pos[1]

                    if abs(dx) > swipe_threshold or abs(dy) > swipe_threshold:
                        if abs(dx) > abs(dy):
                            if dx > 0:
                                print("右スワイプ")
                                current_screen = "boy"
                            else:
                                print("左スワイプ")
                                current_screen = "girl"
                        else:
                            if dy > 0:
                                print("下スワイプ")
                            else:
                                print("上スワイプ")
                    else:
                        print("タップ")

                    start_pos = None
                    end_pos = None

        # 背景色を白に設定
        screen.fill(WHITE)

        # 画面描画
        if current_screen == "boy":
            resized_image = resize_image(current_boy_image, screen_width, screen_height)
            screen.blit(resized_image, (0, 0))
        elif current_screen == "girl":
            resized_image = resize_image(current_girl_image, screen_width, screen_height)
            screen.blit(resized_image, (0, 0))

        # 画面更新
        pygame.display.flip()

    def face_Default():
        if current_screen == "boy":
            current_boy_image = boy_Default_image
        elif current_screen == "girl":
            current_girl_image = girl_Default_image

    def face_sleep():
        if current_screen == "boy":
            current_boy_image = boy_sleep_image
        elif current_screen == "girl":
            current_girl_image = girl_sleep_image

    def face_anger():
        if current_screen == "boy":
            current_boy_image = boy_anger_image
        elif current_screen == "girl":
            current_girl_image = girl_anger_image

    def face_smile():
        if current_screen == "boy":
            current_boy_image = boy_smile_image
        elif current_screen == "girl":
            current_girl_image = girl_smile_image

    def face_thinEye():
        if current_screen == "boy":
            current_boy_image = boy_thinEye_image
        elif current_screen == "girl":
            current_girl_image = girl_thinEye_image

    def face_wink():
        if current_screen == "boy":
            current_boy_image = boy_wink_image
        elif current_screen == "girl":
            current_girl_image = girl_wink_image

    def face_embarrassed():
        if current_screen == "boy":
            current_boy_image = boy_embarrassed_image
        elif current_screen == "girl":
            current_girl_image = girl_embarrassed_image

    def face_sad():
        if current_screen == "boy":
            current_boy_image = boy_sad_image
        elif current_screen == "girl":
            current_girl_image = girl_sad_image

    def face_omg():
        if current_screen == "boy":
            current_boy_image = boy_omg_image
        elif current_screen == "girl":
            current_girl_image = girl_omg_image   

    def face_kirarin():
        if current_screen == "boy":
            current_boy_image = boy_kirarin_image
        elif current_screen == "girl":
            current_girl_image = girl_kirarin_image

    def face_doubt():
        if current_screen == "boy":
            current_boy_image = boy_doubt_image
        elif current_screen == "girl":
            current_girl_image = girl_doubt_image


    # Pygameを終了
    pygame.quit()
    sys.exit()

# 実行
if __name__ == "__main__":
    display()


# #Empath → gpioPin受け取り側
# # 各ピンを監視するためのセットアップ
# calm_pin = Button(0)
# anger_pin = Button(5)
# joy_pin = Button(6)
# sorrow_pin = Button(13)
# energy_pin = Button(5)
# # Pin番号 0,5,6,13
# # def close_eyes():
    

# # 各感情に対応する処理
# def handle_calm():
#     print("Calm (17): 落ち着いた信号を受信しました。")
#     # 必要な処理をここに追加

# def handle_anger():
#     print("Anger (27): 怒りの信号を受信しました。")
#     # 必要な処理をここに追加

# def handle_joy():
#     print("Joy (22): 喜びの信号を受信しました。")
#     # 必要な処理をここに追加

# def handle_sorrow():
#     print("Sorrow (5): 悲しみの信号を受信しました。")
#     # 必要な処理をここに追加

# def handle_energy():
#     print("Energy (6): 活力の信号を受信しました。")
#     # 必要な処理をここに追加

# # ピンに信号が入ったときのイベント設定
# calm_pin.when_pressed = handle_calm
# anger_pin.when_pressed = handle_anger
# joy_pin.when_pressed = handle_joy
# sorrow_pin.when_pressed = handle_sorrow
# energy_pin.when_pressed = handle_energy

# # 無限ループで監視
# print("信号を監視しています。Ctrl+C で終了します。")

# # windowsの場合pause()は使えないから代用
# pause()
# try:
#     while True:
#         pass  # 無限ループで待機
# except KeyboardInterrupt:
#     print("プログラムを終了します。")














# import tkinter as tk
# from PIL import Image, ImageTk
# #原寸大きさ1920x1080
# # メインウィンドウの作成
# root = tk.Tk()
# root.title("タッチイベントで画面推移")

# # ウィンドウの装飾を無効化（タイトルバーを非表示） 
# #root.overrideredirect(True)

# # 画面サイズの設定
# canvas_width, canvas_height = 1920,1080 #960,540にて確認
# root.geometry(f"{canvas_width}x{canvas_height}")

# # 各画面を切り替えるためのフレーム作成
# frames = {}

# def switch_frame(frame_name):
#     """指定されたフレームを表示"""
#     for frame in frames.values():
#         frame.pack_forget()  # すべてのフレームを非表示
#     frames[frame_name].pack(fill=tk.BOTH, expand=True)  # 指定のフレームを表示

# # 画面1: メイン画面
# def create_main_screen():
#     frame = tk.Frame(root)
    
#     # メイン画面用キャンバス
#     canvas = tk.Canvas(frame, width=canvas_width, height=canvas_height)
#     canvas.pack(fill=tk.BOTH, expand=True)
    
#     # 画像を読み込み
#     image_path = "Programs/img/boy_1.jpg"
#     img = Image.open(image_path)
#     img = img.resize((canvas_width, canvas_height))  # 画像のサイズを調整
#     img_tk = ImageTk.PhotoImage(img)
    
#     # 画像をキャンバスに表示
#     canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
#     canvas.image = img_tk  # 画像がガベージコレクションされないように保持
    
#     # メッセージ表示
#     canvas.create_text(canvas_width / 2, canvas_height / 4, text="主人公の性別を選んでください。", font=("Arial", 24), fill="black")

#     # ボタンの領域を描画
#     #rect1 = canvas.create_rectangle(320, 360, 660, 720, fill="red", outline="black") #左、上、右、下 160, 180, 330, 360にて確認
#     canvas.create_text(490, 580, text="男", font=("Arial", 60), fill="black")

#     #rect2 = canvas.create_rectangle(1250, 360, 1600, 720, fill="green", outline="black") #左、上、右、下 625, 180, 800, 360にて確認
#     canvas.create_text(1420, 580, text="女", font=("Arial", 60), fill="black")

#     # タッチイベントのバインド
#     def on_touch(event):
#         if 320 <= event.x <= 660 and 360 <= event.y <= 720: #左、右、上、下
#             print("画面Aに移動します")
#             switch_frame("screen_a")
#         elif 1250 <= event.x <= 1600 and 360 <= event.y <= 720: #左、右、上、下
#             print("画面Bに移動します")
#             switch_frame("screen_b")

#     canvas.bind("<Button-1>", on_touch)  # 左クリックをタッチとして扱う

#     return frame

# # 画面A: 画像Aを表示
# def create_screen_a():
#     frame = tk.Frame(root)
    
#     # 画像を読み込み
#     image_path = "Programs/img/boy_1.jpg"
#     img = Image.open(image_path)
#     img = img.resize((canvas_width, canvas_height))  # 画像のサイズを調整
#     img_tk = ImageTk.PhotoImage(img)
    
#     # 画像をキャンバスに表示
#     canvas = tk.Canvas(frame, width=canvas_width, height=canvas_height)
#     canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
#     canvas.image = img_tk  # 画像がガベージコレクションされないように保持
#     canvas.pack(fill=tk.BOTH, expand=True)
#     canvas.create_text(490, 580, text="戻る", font=("Arial", 60), fill="black") 
#     def on_touch(event): 
#         if 320 <= event.x <= 660 and 360 <= event.y <= 720: # 左、右、上、下 
#             print("メイン画面に戻ります") 
#             switch_frame("main") 

#     canvas.bind("<Button-1>", on_touch) # 左クリックをタッチとして扱う
#     return frame

# # 画面B: 画像Bを表示
# def create_screen_b():
#     frame = tk.Frame(root)
    
#     # 画像を読み込み
#     image_path = "Programs/img/girl_1.jpg"
#     img = Image.open(image_path)
#     img = img.resize((canvas_width, canvas_height))  # 画像のサイズを調整
#     img_tk = ImageTk.PhotoImage(img)
    
#     # 画像をキャンバスに表示
#     canvas = tk.Canvas(frame, width=canvas_width, height=canvas_height)
#     canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
#     canvas.image = img_tk  # 画像がガベージコレクションされないように保持
#     canvas.pack(fill=tk.BOTH, expand=True)
#     canvas.create_text(490, 580, text="戻る", font=("Arial", 60), fill="black")
    
#     # タッチイベントのバインド 
#     def on_touch(event): 
#         if 320 <= event.x <= 660 and 320 <= event.y <= 720: # 左、右、上、下 
#             print("メイン画面に戻ります")
            
#             switch_frame("main") 

#     canvas.bind("<Button-1>", on_touch) # 左クリックをタッチとして扱う
#     return frame

# # フレームを登録
# frames["main"] = create_main_screen()
# frames["screen_a"] = create_screen_a()
# frames["screen_b"] = create_screen_b()

# # 最初の画面を表示
# switch_frame("main")

# """# Shiftキーでアプリケーションを終了 
# def on_shift(event): 
#     if event.keysym == "Shift_L" or event.keysym == "Shift_R": 
#         print("アプリケーションを終了します") 
#         root.destroy() 
# root.bind("<Key>", on_shift)"""

# # Escキーでアプリケーションを終了 
# def on_esc(event): 
#     print("アプリケーションを終了します") 
#     root.destroy() 
# root.bind("<Escape>", on_esc)

# # F1キーでメイン画面に戻る
# def on_f1(event):
#     if event.keysym == "F1":
#         print("メイン画面に戻ります")
#         switch_frame("main")
# root.bind("<KeyPress-F1>", on_f1)

# # メインループ
# root.mainloop()

# #pip install pillow これ入れるかも？


