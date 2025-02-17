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
        main_image = pygame.image.load("Test/sato_test/emobot1.jpg")
        screen_a_image = pygame.image.load("Test/sato_test/emobot1.jpg")
        screen_b_image = pygame.image.load("Test/sato_test/emobot2.jpg")
    except pygame.error as e:
        print(f"画像の読み込みエラー: {e}")
        pygame.quit()
        sys.exit()

    # 画像のサイズを取得してウィンドウサイズを設定
    WIDTH, HEIGHT = main_image.get_width(), main_image.get_height()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))  # ウィンドウの作成
    pygame.display.set_caption("Pygame 画面出力例")  # ウィンドウタイトル

    # フレームの状態管理
    current_screen = "main"

    # スワイプに関連する変数
    # is_swiping = False
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
                # is_swiping = True
                start_pos = event.pos
            elif event.type == pygame.MOUSEBUTTONUP:
                # is_swiping = False
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
            screen.blit(main_image, (0, 0))
        elif current_screen == "screen_a":
            screen.blit(screen_a_image, (0, 0))
        elif current_screen == "screen_b":
            screen.blit(screen_b_image, (0, 0))

        # 画面更新
        pygame.display.flip()

    # Pygameを終了
    pygame.quit()
    sys.exit()

# 実行
if __name__ == "__main__":
    display()
