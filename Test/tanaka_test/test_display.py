import pygame
import os
import sys
# from gpiozero import LED, Button
# from signal import pause

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

    # 現在の画像
    current_boy_image = boy_sleep_image
    current_girl_image = girl_sleep_image

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

# 現在の画面を示す変数（グローバル）
current_screen = "boy"  # 初期状態

def display():
    global current_screen  # グローバル変数を明示

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
                if event.key == pygame.K_ESCAPE:
                    running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                start_pos = event.pos
            elif event.type == pygame.MOUSEBUTTONUP:
                end_pos = event.pos
                dx = end_pos[0] - start_pos[0]

                if abs(dx) > 50:
                    if dx > 0:
                        current_screen = "boy"
                    else:
                        current_screen = "girl"

        screen.fill(WHITE)

        if current_screen == "boy":
            resized_image = resize_image(current_boy_image, screen_width, screen_height)
        else:
            resized_image = resize_image(current_girl_image, screen_width, screen_height)

        screen.blit(resized_image, (0, 0))
        pygame.display.flip()

    pygame.quit()
    sys.exit()

# 実行
if __name__ == "__main__":
    display()

def face_Default():
    global current_boy_image
    global current_girl_image
    if current_screen == "boy":
        current_boy_image = boy_Default_image
    elif current_screen == "girl":
        current_girl_image = girl_Default_image

def face_sleep():
    global current_boy_image
    global current_girl_image
    if current_screen == "boy":
        current_boy_image = boy_sleep_image
    elif current_screen == "girl":
        current_girl_image = girl_sleep_image

def face_anger():
    global current_boy_image
    global current_girl_image
    if current_screen == "boy":
        current_boy_image = boy_anger_image
    elif current_screen == "girl":
        current_girl_image = girl_anger_image

def face_smile():
    global current_boy_image
    global current_girl_image
    if current_screen == "boy":
        current_boy_image = boy_smile_image
    elif current_screen == "girl":
        current_girl_image = girl_smile_image

def face_thinEye():
    global current_boy_image
    global current_girl_image
    if current_screen == "boy":
        current_boy_image = boy_thinEye_image
    elif current_screen == "girl":
        current_girl_image = girl_thinEye_image

def face_wink():
    global current_boy_image
    global current_girl_image
    if current_screen == "boy":
        current_boy_image = boy_wink_image
    elif current_screen == "girl":
        current_girl_image = girl_wink_image

def face_embarrassed():
    global current_boy_image
    global current_girl_image
    if current_screen == "boy":
        current_boy_image = boy_embarrassed_image
    elif current_screen == "girl":
        current_girl_image = girl_embarrassed_image

def face_sad():
    global current_boy_image
    global current_girl_image
    if current_screen == "boy":
        current_boy_image = boy_sad_image
    elif current_screen == "girl":
        current_girl_image = girl_sad_image

def face_omg():
    global current_boy_image
    global current_girl_image
    if current_screen == "boy":
        current_boy_image = boy_omg_image
    elif current_screen == "girl":
        current_girl_image = girl_omg_image   

def face_kirarin():
    global current_boy_image
    global current_girl_image
    if current_screen == "boy":
        current_boy_image = boy_kirarin_image
    elif current_screen == "girl":
        current_girl_image = girl_kirarin_image

def face_doubt():
    global current_boy_image
    global current_girl_image
    if current_screen == "boy":
        current_boy_image = boy_doubt_image
    elif current_screen == "girl":
        current_girl_image = girl_doubt_image
