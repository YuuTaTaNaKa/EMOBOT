import pygame
import os
import sys

def display():
    # Pygameの初期化
    pygame.init()

    # 色の定義 (RGB形式)
    WHITE = (255, 255, 255)

    # 画像の読み込み
    try:
        # main_image = pygame.image.load("C:\\EMOBOT\\Test\\sato_test\\emobot1.jpg")
        # screen_a_image = pygame.image.load("C:\\EMOBOT\\Test\\sato_test\\emobot1.jpg")
        # screen_b_image = pygame.image.load("C:\\EMOBOT\\Test\\sato_test\\emobot2.jpg")

        # boy画像
        boy_Default_image = pygame.image.load("Programs/img/boy_Default.jpg")
        boy_smile_image = pygame.image.load("Programs/img/boy_smile.jpg")
        boy_kirarin_image = pygame.image.load("Programs/img/boy_kirarin.jpg")
        boy_anger_image = pygame.image.load("Programs/img/boy_anger.jpg")
        boy_doubt_image = pygame.image.load("Programs/img/boy_doubt.jpg")
        boy_thinEye_image = pygame.image.load("Programs/img/boy_thinEye.jpg")
        boy_wink_image = pygame.image.load("Programs/img/boy_wink.jpg")
        boy_sleep_image = pygame.image.load("Programs/img/boy_sleep.jpg")
        boy_sad_image = pygame.image.load("Programs/img/boy_sad.jpg")

        # girl画像
        girl_Default_image = pygame.image.load("Programs/img/girl_Default.jpg")
        girl_smile_image = pygame.image.load("Programs/img/girl_smile.jpg")
        girl_kirarin_image = pygame.image.load("Programs/img/girl_kirarin.jpg")
        girl_anger_image = pygame.image.load("Programs/img/girl_anger.jpg")
        girl_doubt_image = pygame.image.load("Programs/img/girl_doubt.jpg")
        girl_thinEye_image = pygame.image.load("Programs/img/girl_thinEye.jpg")
        girl_sleep_image = pygame.image.load("Programs/img/girl_sleep.jpg")
        girl_sad_image = pygame.image.load("Programs/img/girl_sad.jpg")
    except pygame.error as e:
        print(f"画像の読み込みエラー: {e}")
        pygame.quit()
        sys.exit()

    # 画像のサイズを取得してウィンドウサイズを設定
    WIDTH, HEIGHT = boy_Default_image.get_width(), boy_Default_image.get_height()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))  # ウィンドウの作成
    pygame.display.set_caption("Pygame 画面出力例")  # ウィンドウタイトル

    # フレームの状態管理
    current_screen = "main"

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
                                current_screen = "screen_a"
                            else:
                                print("左スワイプ")
                                current_screen = "screen_b"
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
        if current_screen == "main":
            screen.blit(boy_Default_image, (0, 0))
        elif current_screen == "screen_a":
            screen.blit(boy_Default_image, (0, 0))
        elif current_screen == "screen_b":
            screen.blit(girl_Default_image, (0, 0))

        # 画面更新
        pygame.display.flip()

    # Pygameを終了
    pygame.quit()
    sys.exit()

# 実行
if __name__ == "__main__":
    display()




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


