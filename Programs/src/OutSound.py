# 音声出力スレッド
import time
import pygame
import os
from random import choice
import RPi.GPIO as GPIO
import Process

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
    pygame.mixer.init()
    pygame.mixer.music.load(smile_mp3)
    pygame.mixer.music.play(0)
    #print("おはよう")
    return

def greet_afternoon():
    pygame.mixer.init()
    pygame.mixer.music.load(smile_mp3)
    pygame.mixer.music.play(0)
    #print("こんにちは")
    return

def greet_night():
    pygame.mixer.init()
    pygame.mixer.music.load(smile_mp3)
    pygame.mixer.music.play(0)
    #print("こんばんは")
    return

def bye():
    pygame.mixer.init()
    pygame.mixer.music.load(smile_mp3)
    pygame.mixer.music.play(0)
    #print("さようなら")
    return

def im_going():
    pygame.mixer.init()
    pygame.mixer.music.load(smile_mp3)
    pygame.mixer.music.play(0)
    #print("いってきます")
    return

def welcome_home():
    pygame.mixer.init()
    pygame.mixer.music.load(smile_mp3)
    pygame.mixer.music.play(0)
    #print("おかえりなさい")
    return

def good_night():
    pygame.mixer.init()
    pygame.mixer.music.load(smile_mp3)
    pygame.mixer.music.play(0)
    #print("おやすみ")
    return

#「感情」************************************************************* 

def happy():
    pygame.mixer.init()
    pygame.mixer.music.load(smile_mp3)
    pygame.mixer.music.play(0)
    # print("うれしい")
    return

def sad():
    pygame.mixer.init()
    pygame.mixer.music.load(sad_mp3)
    pygame.mixer.music.play(0)
    # print("悲しい")
    return

def surprise():
    pygame.mixer.init()
    pygame.mixer.music.load(omg_mp3)
    pygame.mixer.music.play(0)
    # print("驚き")
    return

def fear():
    pygame.mixer.init()
    pygame.mixer.music.load(omg_mp3)
    pygame.mixer.music.play(0)
    # print("恐れ")
    return


#「Music」*************************************************************  

def playMusic():
    pygame.mixer.init()
    pygame.mixer.music.load(choice(Musics))
    pygame.mixer.music.play(-1)
    # print("音楽を再生します")
    Process.current_process = "music"
    return

def stopMusic():
    pygame.mixer.music.stop()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(24, GPIO.OUT, pull_up_down=GPIO.PUD_DOWN)
    GPIO.output(24, GPIO.HIGH)
    time.sleep(3)
    GPIO.output(24, GPIO.LOW)
    # print("音楽を停止します")
    return

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
