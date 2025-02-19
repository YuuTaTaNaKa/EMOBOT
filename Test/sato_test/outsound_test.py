import pygame

# ① pygameのミキサーを初期化
pygame.mixer.init()
print("音声を再生します")
# ② 音声ファイルをロード
pygame.mixer.music.load("167.mp3")  # または .wav / .ogg など
print("音声を再生します")
# ③ 再生
pygame.mixer.music.play(1)

# ④ 再生が終わるまで待つ（省略可能）
while pygame.mixer.music.get_busy():
    pass
