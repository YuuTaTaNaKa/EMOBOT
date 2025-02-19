import pygame
import os
import sys
import OutSound
import RPi.GPIO as GPIO
# from gpiozero import LED, Button
# from signal import pause

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(0, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)

try:
    #pathの読み込み
    base_path = os.path.join("Programs","img")

    # boy画像
    boy_Default_image = pygame.image.load(os.path.join(os.path.dirname(__file__), "..", "img", "boy_Default.jpg"))
    boy_smile_image = pygame.image.load(os.path.join(os.path.dirname(__file__), "..", "img", "boy_smile.jpg"))
    boy_kirarin_image = pygame.image.load(os.path.join(os.path.dirname(__file__), "..", "img", "boy_kirarin.jpg"))
    boy_anger_image = pygame.image.load(os.path.join(os.path.dirname(__file__), "..", "img", "boy_anger.jpg"))
    boy_doubt_image = pygame.image.load(os.path.join(os.path.dirname(__file__), "..", "img", "boy_doubt.jpg"))
    boy_embarrassed_image = pygame.image.load(os.path.join(os.path.dirname(__file__), "..", "img", "boy_embarrassed.jpg"))
    boy_thinEye_image = pygame.image.load(os.path.join(os.path.dirname(__file__), "..", "img", "boy_thinEye.jpg"))
    boy_wink_image = pygame.image.load(os.path.join(os.path.dirname(__file__), "..", "img", "boy_wink.jpg"))
    boy_sleep_image = pygame.image.load(os.path.join(os.path.dirname(__file__), "..", "img", "boy_sleep.jpg"))
    boy_sad_image = pygame.image.load(os.path.join(os.path.dirname(__file__), "..", "img", "boy_sad.jpg"))
    boy_omg_image = pygame.image.load(os.path.join(os.path.dirname(__file__), "..", "img", "boy_omg.jpg"))
    # girl画像
    girl_Default_image = pygame.image.load(os.path.join(os.path.dirname(__file__), "..", "img", "girl_Default.jpg"))
    girl_smile_image = pygame.image.load(os.path.join(os.path.dirname(__file__), "..", "img", "girl_smile.jpg"))
    girl_kirarin_image = pygame.image.load(os.path.join(os.path.dirname(__file__), "..", "img", "girl_kirarin.jpg"))
    girl_anger_image = pygame.image.load(os.path.join(os.path.dirname(__file__), "..", "img", "girl_anger.jpg"))
    girl_doubt_image = pygame.image.load(os.path.join(os.path.dirname(__file__), "..", "img", "girl_doubt.jpg"))
    girl_embarrassed_image = pygame.image.load(os.path.join(os.path.dirname(__file__), "..", "img", "girl_embarrassed.jpg"))
    girl_thinEye_image = pygame.image.load(os.path.join(os.path.dirname(__file__), "..", "img", "girl_thinEye.jpg"))
    girl_wink_image = pygame.image.load(os.path.join(os.path.dirname(__file__), "..", "img", "girl_wink.jpg"))
    girl_sleep_image = pygame.image.load(os.path.join(os.path.dirname(__file__), "..", "img", "girl_sleep.jpg"))
    girl_sad_image = pygame.image.load(os.path.join(os.path.dirname(__file__), "..", "img", "girl_sad.jpg"))
    girl_omg_image = pygame.image.load(os.path.join(os.path.dirname(__file__), "..", "img", "girl_omg.jpg"))

    # 初期状態を sleep にする
    current_process = "sleep"
    current_boy_image = boy_sleep_image
    current_girl_image = girl_sleep_image

    # while running: 内の GPIO処理
    if GPIO.input(25) == GPIO.HIGH:  # sleepコマンドを受け付けた時
        current_process = "sleep"
        current_boy_image = boy_sleep_image
        current_girl_image = girl_sleep_image  # 追加 (girlもsleepにする)

    
    
    # 現在の画像
    current_boy_image = boy_sleep_image
    current_girl_image = girl_sleep_image

    # 現在の画面を示す変数（グローバル）
    current_screen = "boy"  # 初期状態
    # 現在の処理を保持する変数
    current_process = "sleep"

    

except pygame.error as e:
    print(f"画像の読み込みエラー: {e}")
    # LED.led_error()
    pygame.quit()
    sys.exit()

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
    global current_screen, current_process # グローバル変数を明示
    global current_boy_image, current_girl_image

    pygame.init()
    WHITE = (255, 255, 255)

    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    screen_width, screen_height = screen.get_size()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  #終了コマンド
                    running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:  #開始座標
                start_pos = event.pos
            elif event.type == pygame.MOUSEBUTTONUP:  #終了座標
                end_pos = event.pos
                dx = end_pos[0] - start_pos[0]
                
                #sleep状態かつ50以上スワイプした時
                if abs(dx) > 50 and current_process == "sleep":
                    if dx > 0:
                        current_screen = "boy"
                    else:
                        current_screen = "girl"
                #タップイベントの処理
                else:
                    if current_process == "sleep":  #sleep状態の時
                        GPIO.output(5, GPIO.HIGH)
                        current_boy_image = boy_Default_image
                    elif current_process == "accept": #コマンド受付時にタッチされた時
                        GPIO.output(0, GPIO.HIGH)
                        if current_screen == "boy":   #喜ぶ
                            current_boy_image = boy_smile_image  
                        else:
                            current_girl_image = girl_smile_image
                    
                    current_process = "execution"

        #mainからの信号を受信したとき
        if GPIO.input(23) == GPIO.HIGH:  #エモボットを受け付けた時
            current_process = "accept"

        if GPIO.input(24) == GPIO.HIGH:  #処理に移行した時
            current_process = "execution"

        if GPIO.input(25) == GPIO.HIGH:  #sleepコマンドを受け付けた時
            current_process = "sleep"
            current_boy_image = boy_sleep_image

        if GPIO.input(8) == GPIO.HIGH:   #smile
            if current_screen == "boy":
                current_boy_image = boy_smile_image
            else:
                current_girl_image = girl_smile_image
        elif GPIO.input(8) == GPIO.LOW:
            if current_screen == "boy":
                current_boy_image = boy_Default_image
            else:
                current_girl_image = girl_Default_image

        if GPIO.input(7) == GPIO.HIGH:   #kirarin
            if current_screen == "boy":
                current_boy_image = boy_kirarin_image
            else:
                current_girl_image = girl_kirarin_image
        elif GPIO.input(7) == GPIO.LOW:
            if current_screen == "boy":
                current_boy_image = boy_Default_image
            else:
                current_girl_image = girl_Default_image

        if GPIO.input(1) == GPIO.HIGH:   #emmbarrassed
            if current_screen == "boy":
                current_boy_image = boy_embarrassed_image
            else:
                current_girl_image = girl_embarrassed_image
        elif GPIO.input(1) == GPIO.LOW:
            if current_screen == "boy":
                current_boy_image = boy_Default_image
            else:
                current_girl_image = girl_Default_image

        if GPIO.input(12) == GPIO.HIGH:   #sad
            if current_screen == "boy":
                current_boy_image = boy_sad_image
            else:
                current_girl_image = girl_sad_image
        elif GPIO.input(12) == GPIO.LOW:
            if current_screen == "boy":
                current_boy_image = boy_Default_image
            else:
                current_girl_image = girl_Default_image

        if GPIO.input(16) == GPIO.HIGH:   #wink
            if current_screen == "boy":
                current_boy_image = boy_wink_image
            else:
                current_girl_image = girl_wink_image
        elif GPIO.input(16) == GPIO.LOW:
            if current_screen == "boy":
                current_boy_image = boy_Default_image
            else:
                current_girl_image = girl_Default_image

        if GPIO.input(20) == GPIO.HIGH:   #thinEye
            if current_screen == "boy":
                current_boy_image = boy_smile_image
            else:
                current_girl_image = girl_smile_image
        elif GPIO.input(20) == GPIO.LOW:
            if current_screen == "boy":
                current_boy_image = boy_Default_image
            else:
                current_girl_image = girl_Default_image

        if GPIO.input(19) == GPIO.HIGH:   #omg
            if current_screen == "boy":
                current_boy_image = boy_omg_image
            else:
                current_girl_image = girl_omg_image
        elif GPIO.input(19) == GPIO.LOW:
            if current_screen == "boy":
                current_boy_image = boy_Default_image
            else:
                current_girl_image = girl_Default_image

        if GPIO.input(13) == GPIO.HIGH:   #doubt
            if current_screen == "boy":
                current_boy_image = boy_doubt_image
            else:
                current_girl_image = girl_doubt_image
        elif GPIO.input(13) == GPIO.LOW:
            if current_screen == "boy":
                current_boy_image = boy_Default_image
            else:
                current_girl_image = girl_Default_image

        if GPIO.input(6) == GPIO.HIGH:   #anger
            if current_screen == "boy":
                current_boy_image = boy_anger_image
            else:
                current_girl_image = girl_anger_image
        elif GPIO.input(6) == GPIO.LOW:
            if current_screen == "boy":
                current_boy_image = boy_Default_image
            else:
                current_girl_image = girl_Default_image

        screen.fill(WHITE)

        # 画面の切り替え
        if current_screen == "boy":
            resized_image = resize_image(current_boy_image, screen_width, screen_height)
        else:
            resized_image = resize_image(current_girl_image, screen_width, screen_height)

        screen.fill(WHITE)
        screen.blit(resized_image, (0, 0))
        pygame.display.flip()

    pygame.quit()
    # GPIO.cleanup()
    sys.exit()

# 実行
if __name__ == "__main__":
    display()
    
"""
pin
mein  disp  動作するもの
23    23    acceptの受け取り
24    24    executionの受け取り
25    25    sleepの受け取り
 8     8    smileの受け取り
 7     7    kirarinの受け取り
 1     1    embarrassedの受け取り
12    12    sadの受け取り
16    16    winkの受け取り
20    20    thinEyeの受け取り
19    19    omgの受け取り
13    13    doubtの受け取り
 6     6    angerの受け取り
 5     5    sleep時に画面タッチしたときに信号を出力
 0     0    accept時に画面タッチしたときに信号を出力
11     9
"""

# import pygame
# import os
# import sys
# import OutSound
# # from gpiozero import LED, Button
# # from signal import pause

# # 画像をロードする関数
# def load_images():
#     """画像を読み込み、辞書に格納する"""
#     emotions = ["Default", "smile", "kirarin", "anger", "doubt", "embarrassed", 
#                 "thinEye", "wink", "sleep", "sad", "omg"]
    
#     base_path = os.path.join(os.path.dirname(__file__), "..", "img")
    
#     try:
#         boy_images = {emo: pygame.image.load(os.path.join(base_path, f"boy_{emo}.jpg")) for emo in emotions}
#         girl_images = {emo: pygame.image.load(os.path.join(base_path, f"girl_{emo}.jpg")) for emo in emotions}
#     except pygame.error as e:
#         print(f"画像の読み込みエラー: {e}")
#         pygame.quit()
#         sys.exit()

#     return boy_images, girl_images

# # 画像をフルスクリーンにリサイズする関数
# def resize_image(image, screen_width, screen_height):
#     """画像をフルスクリーンに合わせてリサイズする"""
#     img_width, img_height = image.get_size()
#     aspect_ratio = img_width / img_height

#     if screen_width / screen_height > aspect_ratio:
#         new_width, new_height = int(screen_height * aspect_ratio), screen_height
#     else:
#         new_width, new_height = screen_width, int(screen_width / aspect_ratio)

#     return pygame.transform.scale(image, (new_width, new_height))

# # 画面を描画する関数
# def draw_screen(screen, image, screen_width, screen_height):
#     """画面をクリアし、画像を描画する"""
#     screen.fill((255, 255, 255))
#     resized_image = resize_image(image, screen_width, screen_height)
#     screen.blit(resized_image, (0, 0))
#     pygame.display.flip()

# # 画面の切り替えを処理する関数
# def switch_screen(current_screen):
#     """画面を切り替える"""
#     return "girl" if current_screen == "boy" else "boy"

# # イベント処理を行う関数
# def handle_events(current_process, current_screen, boy_images, girl_images):
#     """イベントを処理し、現在の状態を更新する"""
#     start_pos = None  # スワイプ開始位置を記録

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             return False, current_process, current_screen

#         elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
#             return False, current_process, current_screen

#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             start_pos = event.pos  # スワイプ開始位置を記録

#         elif event.type == pygame.MOUSEBUTTONUP and start_pos:
#             end_pos = event.pos
#             dx = end_pos[0] - start_pos[0]

#             # sleep の時だけ boy/girl を変更可能
#             if current_process == "sleep" and abs(dx) > 50:
#                 current_screen = switch_screen(current_screen)

#         # accept の場合はタッチで笑顔に変更
#         if event.type == pygame.MOUSEBUTTONDOWN and current_process == "accept":
#             if current_screen == "boy":
#                 boy_images["current"] = boy_images["smile"]
#             else:
#                 girl_images["current"] = girl_images["smile"]
            
#             # OutSound.happy()  # 音声再生
#             current_process = "execution"

#     return True, current_process, current_screen

# # メインの表示処理
# def display():
#     pygame.init()
#     screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
#     screen_width, screen_height = screen.get_size()

#     # 画像を読み込む
#     boy_images, girl_images = load_images()
#     boy_images["current"] = boy_images["sleep"]
#     girl_images["current"] = girl_images["sleep"]

#     current_screen = "boy"  # 初期画面
#     current_process = "sleep"  # 初期状態は sleep
#     running = True

#     while running:
#         running, current_process, current_screen = handle_events(current_process, current_screen, boy_images, girl_images)

#         if current_screen == "boy":
#             draw_screen(screen, boy_images["current"], screen_width, screen_height)
#         else:
#             draw_screen(screen, girl_images["current"], screen_width, screen_height)

#     pygame.quit()
#     sys.exit()

# # 実行
# if __name__ == "__main__":
#     display()



# def face_Default():
#     global current_boy_image
#     global current_girl_image
#     if current_screen == "boy":
#         current_boy_image = boy_Default_image
#     elif current_screen == "girl":
#         current_girl_image = girl_Default_image

# def face_sleep():
#     global current_boy_image
#     global current_girl_image
#     if current_screen == "boy":
#         current_boy_image = boy_sleep_image
#     elif current_screen == "girl":
#         current_girl_image = girl_sleep_image

# def face_anger():
#     global current_boy_image
#     global current_girl_image
#     if current_screen == "boy":
#         current_boy_image = boy_anger_image
#     elif current_screen == "girl":
#         current_girl_image = girl_anger_image

# def face_smile():
#     global current_boy_image
#     global current_girl_image
#     if current_screen == "boy":
#         current_boy_image = boy_smile_image
#     elif current_screen == "girl":
#         current_girl_image = girl_smile_image

# def face_thinEye():
#     global current_boy_image
#     global current_girl_image
#     if current_screen == "boy":
#         current_boy_image = boy_thinEye_image
#     elif current_screen == "girl":
#         current_girl_image = girl_thinEye_image

# def face_wink():
#     global current_boy_image
#     global current_girl_image
#     if current_screen == "boy":
#         current_boy_image = boy_wink_image
#     elif current_screen == "girl":
#         current_girl_image = girl_wink_image

# def face_embarrassed():
#     global current_boy_image
#     global current_girl_image
#     if current_screen == "boy":
#         current_boy_image = boy_embarrassed_image
#     elif current_screen == "girl":
#         current_girl_image = girl_embarrassed_image

# def face_sad():
#     global current_boy_image
#     global current_girl_image
#     if current_screen == "boy":
#         current_boy_image = boy_sad_image
#     elif current_screen == "girl":
#         current_girl_image = girl_sad_image

# def face_omg():
#     global current_boy_image
#     global current_girl_image
#     if current_screen == "boy":
#         current_boy_image = boy_omg_image
#     elif current_screen == "girl":
#         current_girl_image = girl_omg_image   

# def face_kirarin():
#     global current_boy_image
#     global current_girl_image
#     if current_screen == "boy":
#         current_boy_image = boy_kirarin_image
#     elif current_screen == "girl":
#         current_girl_image = girl_kirarin_image

# def face_doubt():
#     global current_boy_image
#     global current_girl_image
#     if current_screen == "boy":
#         current_boy_image = boy_doubt_image
#     elif current_screen == "girl":
#         current_girl_image = girl_doubt_image

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

