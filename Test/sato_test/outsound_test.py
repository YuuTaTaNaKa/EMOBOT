import pygame

# ① pygameのミキサーを初期化
pygame.mixer.init()

# ② 音声ファイルをロード
pygame.mixer.music.load("kirarin.mp3")  # または .wav / .ogg など

# ③ 再生
pygame.mixer.music.play()

# ④ 再生が終わるまで待つ（省略可能）
while pygame.mixer.music.get_busy():
    pass
