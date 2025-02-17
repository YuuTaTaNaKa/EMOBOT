# 音声出力スレッド
import time
import pygame
import os
from random import choice

#「あかりん音声ファイルパス」

anger_mp3 = os.path.join(os.path.dirname(__file__), "..", "se", "anger.mp3")
doubt_mp3 = os.path.join(os.path.dirname(__file__), "..", "se", "doubt.mp3")
embarrassed_mp3 = os.path.join(os.path.dirname(__file__), "..", "se", "embarrassed.mp3")
kirarin_mp3 = os.path.join(os.path.dirname(__file__), "..", "se", "kirarin.mp3")
omg_mp3 = os.path.join(os.path.dirname(__file__), "..", "se", "omg.mp3")
sad_mp3 = os.path.join(os.path.dirname(__file__), "..", "se", "sad.mp3")
smile_mp3 = os.path.join(os.path.dirname(__file__), "..", "se", "smile.mp3")
testsound_scream_mp3 = os.path.join(os.path.dirname(__file__), "..", "se", "testsound_scream.mp3")

#「機能」*************************

#音楽を再生
Musics = [os.path.join(os.path.dirname(__file__), "..", "se", "167.mp3"),
           ""]

# -------------------------------〈メソッド〉--------------------------------


#「挨拶」*************************************************************   

def greet_morning():
    pygame.mixer.music.load(smile_mp3)
    #print("おはよう")
    return

def greet_afternoon():
    pygame.mixer.music.load(smile_mp3)
    #print("こんにちは")
    return

def greet_night():
    pygame.mixer.music.load(smile_mp3)
    #print("こんばんは")
    return

def bye():
    pygame.mixer.music.load(smile_mp3)
    #print("さようなら")
    return

def im_going():
    pygame.mixer.music.load(smile_mp3)
    #print("いってきます")
    return

def welcome_home():
    pygame.mixer.music.load(smile_mp3)
    #print("おかえりなさい")
    return

def good_night():
    pygame.mixer.music.load(smile_mp3)
    #print("おやすみ")
    return

#「感情」************************************************************* 

def happy():
    pygame.mixer.music.load(smile_mp3)
    # print("うれしい")
    return

def sad():
    pygame.mixer.music.load(sad_mp3)
    # print("悲しい")
    return

def surprise():
    pygame.mixer.music.load(omg_mp3)
    # print("驚き")
    return

def fear():
    pygame.mixer.music.load(omg_mp3)
    # print("恐れ")
    return


#「Music」*************************************************************  
def initialize_pygame():
    pygame.mixer.init()

def playMusic():
    pygame.mixer.music.load(choice(Musics))
    pygame.mixer.music.play()

def stopMusic():
    pygame.mixer.music.stop()

# 汎用処理
def stop():
    # print("停止")
    return


#「感情」************************************************************* 
# def happy():
#     playsound(smile_mp3)
#     # print("うれしい")
#     return

# def sad():
#     playsound(sad_mp3)
#     # print("悲しい")
#     return

# def surprise():
#     playsound(omg_mp3)
#     # print("驚き")
#     return

# def fear():
#     playsound(omg_mp3)
#     # print("恐れ")
#     return

# #「利用者からの返事」*************************************************************  

# def no():
#     playsound(doubt_mp3)
#     # print("わかりません")
#     return

# def ok():
#     playsound(doubt_mp3)
#     # print("わかりました")
#     return

"""pip install pygame"""