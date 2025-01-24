import pygame
import os

def display():
    # 初期設定
    pygame.init()
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("タッチイベントで画面推移")

    # 画像の読み込み
    def load_image(path):
        full_path = os.path.join("Programs", "img", path)
        return pygame.transform.scale(pygame.image.load(full_path), (screen_width, screen_height))

    main_image = load_image("/home/emobot/Desktop/EMOBOT/Test/sato_test/emobot1.jpg")
    screen_a_image = load_image("/home/emobot/Desktop/EMOBOT/Test/sato_test/emobot1.jpg")
    screen_b_image = load_image("/home/emobot/Desktop/EMOBOT/Test/sato_test/emobot2.jpg")

    # フレームの状態管理
    current_screen = "main"

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # 左クリックまたはタップ
                x, y = event.pos
                
                if current_screen == "main":
                    if 100 <= x <= 300 and 300 <= y <= 400:
                        print("画面Aに移動します")
                        current_screen = "screen_a"
                    elif 500 <= x <= 700 and 300 <= y <= 400:
                        print("画面Bに移動します")
                        current_screen = "screen_b"
                elif current_screen in ["screen_a", "screen_b"]:
                    # 画面AまたはBでは、クリックでメイン画面に戻る
                    print("メイン画面に戻ります")
                    current_screen = "main"

        # 画面の描画
        if current_screen == "main":
            screen.blit(main_image, (0, 0))
            
            # ボタンの描画
            pygame.draw.rect(screen, (255, 0, 0), (100, 300, 200, 100))  # 赤いボタン
            pygame.draw.rect(screen, (0, 255, 0), (500, 300, 200, 100))  # 緑のボタン

            # ボタンのテキスト
            font = pygame.font.Font(None, 36)
            text_male = font.render("男", True, (255, 255, 255))
            text_female = font.render("女", True, (255, 255, 255))
            screen.blit(text_male, (170, 335))
            screen.blit(text_female, (570, 335))

        elif current_screen == "screen_a":
            screen.blit(screen_a_image, (0, 0))
            
            # 戻るボタンのテキスト
            font = pygame.font.Font(None, 36)
            text_back = font.render("メイン画面に戻る", True, (0, 0, 0))
            screen.blit(text_back, (screen_width // 2 - 100, screen_height - 50))

        elif current_screen == "screen_b":
            screen.blit(screen_b_image, (0, 0))
            
            # 戻るボタンのテキスト
            font = pygame.font.Font(None, 36)
            text_back = font.render("メイン画面に戻る", True, (0, 0, 0))
            screen.blit(text_back, (screen_width // 2 - 100, screen_height - 50))

        # 画面更新
        pygame.display.flip()

    pygame.quit()

# 実行
if __name__ == "__main__":
    display()
