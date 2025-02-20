import pygame

pygame.mixer.init()  # 初期化

# 効果音をロード
se = pygame.mixer.Sound("/home/emobot2/Desktop/EMOBOT/Test/sato_test/kirarin_PitchChanger.wav")

# 効果音を再生
se.play()
