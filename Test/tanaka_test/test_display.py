import pygame
import os
import sys
# import OutSound
# from gpiozero import LED, Button
# from signal import pause

# 画像をロードする関数
def load_images():
    """画像を読み込み、辞書に格納する"""
    emotions = ["Default", "smile", "kirarin", "anger", "doubt", "embarrassed", 
                "thinEye", "wink", "sleep", "sad", "omg"]
    
    base_path = os.path.join(os.path.dirname(__file__), "..", "img")
    
    try:
        boy_images = {emo: pygame.image.load(os.path.join(base_path, f"boy_{emo}.jpg")) for emo in emotions}
        girl_images = {emo: pygame.image.load(os.path.join(base_path, f"girl_{emo}.jpg")) for emo in emotions}
    except pygame.error as e:
        print(f"画像の読み込みエラー: {e}")
        pygame.quit()
        sys.exit()

    return boy_images, girl_images

# 画像をフルスクリーンにリサイズする関数
def resize_image(image, screen_width, screen_height):
    """画像をフルスクリーンに合わせてリサイズする"""
    img_width, img_height = image.get_size()
    aspect_ratio = img_width / img_height

    if screen_width / screen_height > aspect_ratio:
        new_width, new_height = int(screen_height * aspect_ratio), screen_height
    else:
        new_width, new_height = screen_width, int(screen_width / aspect_ratio)

    return pygame.transform.scale(image, (new_width, new_height))

# 画面を描画する関数
def draw_screen(screen, image, screen_width, screen_height):
    """画面をクリアし、画像を描画する"""
    screen.fill((255, 255, 255))
    resized_image = resize_image(image, screen_width, screen_height)
    screen.blit(resized_image, (0, 0))
    pygame.display.flip()

# 画面の切り替えを処理する関数
def switch_screen(current_screen, dx):
    """スワイプ方向に応じて画面を切り替える"""
    return "boy" if dx > 0 else "girl"

# イベント処理を行う関数
def handle_events(current_process, current_screen, boy_images, girl_images):
    """イベントを処理し、現在の状態を更新する"""
    start_pos = None

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False, current_process, current_screen

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            return False, current_process, current_screen

        elif event.type == pygame.MOUSEBUTTONDOWN:
            start_pos = event.pos

        elif event.type == pygame.MOUSEBUTTONUP and start_pos:
            end_pos = event.pos
            dx = end_pos[0] - start_pos[0]
            if abs(dx) > 50:
                current_screen = switch_screen(current_screen, dx)

        elif event.type == pygame.MOUSEBUTTONDOWN and current_process == "accept":
            if current_screen == "boy":
                boy_images["current"] = boy_images["smile"]
            else:
                girl_images["current"] = girl_images["smile"]
            
            # OutSound.happy()  # 音声再生
            current_process = "execution"

    return True, current_process, current_screen

# メインの表示処理
def display():
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    screen_width, screen_height = screen.get_size()

    # 画像を読み込む
    boy_images, girl_images = load_images()
    boy_images["current"] = boy_images["sleep"]
    girl_images["current"] = girl_images["sleep"]

    current_screen = "boy"  # 初期画面
    current_process = "accept"
    running = True

    while running:
        running, current_process, current_screen = handle_events(current_process, current_screen, boy_images, girl_images)

        if current_screen == "boy":
            draw_screen(screen, boy_images["current"], screen_width, screen_height)
        else:
            draw_screen(screen, girl_images["current"], screen_width, screen_height)

    pygame.quit()
    sys.exit()

# 実行
if __name__ == "__main__":
    display()
