import pygame
import sys

# Pygameの初期化
pygame.init()

# 画面サイズの設定
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("スワイプ機能デモ")

# 色の定義
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# フレームレート制御用のクロック
clock = pygame.time.Clock()

# スワイプに関連する変数
is_swiping = False
start_pos = None
end_pos = None
swipe_threshold = 50  # スワイプと判定する最低距離

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # マウスボタンが押されたとき
        if event.type == pygame.MOUSEBUTTONDOWN:
            is_swiping = True
            start_pos = event.pos

        # マウスボタンが離されたとき
        if event.type == pygame.MOUSEBUTTONUP:
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
                        else:
                            print("左スワイプ")
                    else:
                        if dy > 0:
                            print("下スワイプ")
                        else:
                            print("上スワイプ")
                start_pos = None
                end_pos = None

    # 画面の描画
    screen.fill(WHITE)

    # スワイプ中の線を描画
    if is_swiping and start_pos:
        current_pos = pygame.mouse.get_pos()
        pygame.draw.line(screen, BLUE, start_pos, current_pos, 3)

    pygame.display.flip()
    clock.tick(60)
