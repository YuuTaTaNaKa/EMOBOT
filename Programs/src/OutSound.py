# 音声出力スレッド
import time
import pygame
import os
from random import choice
import RPi.GPIO as GPIO
import Process
import threading

#GPIO設定
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(1, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)

#「あかりん音声ファイルパス」

anger_wav = os.path.join(os.path.dirname(__file__), "..", "se", "anger_Pitch Changer.wav")
doubt_wav = os.path.join(os.path.dirname(__file__), "..", "se", "doubt_Pitch Changer.wav")
embarrassed_wav = os.path.join(os.path.dirname(__file__), "..", "se", "embarrassed_Pitch Changer.wav")
kirarin_wav = os.path.join(os.path.dirname(__file__), "..", "se", "kirarin_Pitch Changer.wav")
omg_wav = os.path.join(os.path.dirname(__file__), "..", "se", "omg_Pitch Changer.wav")
sad_wav = os.path.join(os.path.dirname(__file__), "..", "se", "sad_Pitch Changer.wav")
smile_wav = os.path.join(os.path.dirname(__file__), "..", "se", "smile_Pitch Changer.wav")
testsound_scream_wav = os.path.join(os.path.dirname(__file__), "..", "se", "testsound_scream.mp3")

#「機能」*************************

#音楽を再生
Musics = [os.path.join(os.path.dirname(__file__), "..", "se", "167.mp3"),
          os.path.join(os.path.dirname(__file__), "..", "se", "2_23AM_2.mp3"),
          os.path.join(os.path.dirname(__file__), "..", "se", "303PM_230312.mp3"),
          os.path.join(os.path.dirname(__file__), "..", "se", "Cassette_Tape_Dream.mp3"),
          os.path.join(os.path.dirname(__file__), "..", "se", "Culture.mp3")]

# -------------------------------〈メソッド〉--------------------------------

#「感情」************************************************************* 

def voice_smile():
    pygame.mixer.init()
    # pygame.mixer.music.load(smile_wav)
    # pygame.mixer.music.play(0)
    pygame.mixer.Sound(smile_wav).play()
    # print("うれしい")
    pinSend_sleep()
    return

def voice_sad():
    pygame.mixer.init()
    # pygame.mixer.music.load(sad_wav)
    # pygame.mixer.music.play(0)
    # print("悲しい")
    pygame.mixer.Sound(sad_wav).play()
    pinSend_sleep()
    return

def voise_omg():
    pygame.mixer.init()
    # pygame.mixer.music.load(omg_wav)
    # pygame.mixer.music.play(0)
    pygame.mixer.Sound(omg_wav).play()
    # print("驚き")
    pinSend_sleep()
    return

def voice_kirarin():
    pygame.mixer.init()
    # pygame.mixer.music.load(kirarin_wav)
    # pygame.mixer.music.play(0)
    pygame.mixer.Sound(kirarin_wav).play()
    # print("うれしい")
    pinSend_sleep()
    return

def voice_anger():
    pygame.mixer.init()
    # pygame.mixer.music.load(anger_wav)
    # pygame.mixer.music.play(0)
    pygame.mixer.Sound(anger_wav).play()
    # print("うれしい")
    pinSend_sleep()
    return

def voice_doubt():
    pygame.mixer.init()
    # pygame.mixer.music.load(doubt_wav)
    # pygame.mixer.music.play(0)
    pygame.mixer.Sound(doubt_wav).play()
    # print("うれしい")
    pinSend_sleep()
    return

def voice_embarrassed():
    pygame.mixer.init()
    # pygame.mixer.music.load(embarrassed_wav)
    # pygame.mixer.music.play(0)
    pygame.mixer.Sound(embarrassed_wav).play()
    # print("うれしい")
    pinSend_sleep()
    return

#「Music」*************************************************************  

# def playMusic():
#     pygame.mixer.init()
#     pygame.mixer.music.load(choice(Musics))
#     pygame.mixer.music.set_volume(0.2)
#     pygame.mixer.music.play(-1)
#     # print("音楽を再生します")
#     # Process.current_process = "music"
#     pygame.mixer.fadeout(3000)
#     time.sleep(30)
#     Process.current_music()
#     return

def playMusic():
    pygame.mixer.init()
    
    if not Musics:
        print("エラー: 音楽ファイルが見つかりません！")
        return

    music_file = choice(Musics)
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)  # ループ再生

    print(f"再生中: {music_file}")

    # **30秒後にフェードアウトを実行するスレッドを開始**
    threading.Thread(target=delayed_fadeout, daemon=True).start()
    pinSend_sleep()
    Process.current_music()
def delayed_fadeout():
    """30秒待ってから3秒かけてフェードアウト"""
    time.sleep(10)
    print("フェードアウト開始")
    pygame.mixer.music.fadeout(3000)

def stopMusic():
    pygame.mixer.music.stop()
    # GPIO.setmode(GPIO.BCM)
    # GPIO.setup(24, GPIO.OUT, pull_up_down=GPIO.PUD_DOWN)
    # GPIO.output(24, GPIO.HIGH)
    time.sleep(3)
    # GPIO.output(24, GPIO.LOW)
    # print("音楽を停止します")
    pinSend_sleep()
    return

def pinSend_sleep():
    GPIO.output(25, GPIO.HIGH)
    time.sleep(3)
    GPIO.output(25, GPIO.LOW)
    # Process.current_process = "sleep"
    Process.current_sleep()
    return

# 汎用処理
def stop():
    # print("停止")
    return

# #「挨拶」*************************************************************   

# def greet_morning():
#     pygame.mixer.init()
#     pygame.mixer.music.load(smile_wav)
#     pygame.mixer.music.play(0)
#     #print("おはよう")
#     pinSend_sleep()
#     return

# def greet_afternoon():
#     pygame.mixer.init()
#     pygame.mixer.music.load(smile_wav)
#     pygame.mixer.music.play(0)
#     #print("こんにちは")
#     pinSend_sleep()
#     return

# def greet_night():
#     pygame.mixer.init()
#     pygame.mixer.music.load(smile_wav)
#     pygame.mixer.music.play(0)
#     #print("こんばんは")
#     pinSend_sleep()
#     return

# def bye():
#     pygame.mixer.init()
#     pygame.mixer.music.load(smile_wav)
#     pygame.mixer.music.play(0)
#     #print("さようなら")]
#     pinSend_sleep()
#     return

# def im_going():
#     pygame.mixer.init()
#     pygame.mixer.music.load(smile_wav)
#     pygame.mixer.music.play(0)
#     #print("いってきます")
#     pinSend_sleep()
#     return

# def welcome_home():
#     pygame.mixer.init()
#     pygame.mixer.music.load(smile_wav)
#     pygame.mixer.music.play(0)
#     #print("おかえりなさい")
#     pinSend_sleep()
#     return

# def good_night():
#     pygame.mixer.init()
#     pygame.mixer.music.load(smile_wav)
#     pygame.mixer.music.play(0)
#     #print("おやすみ")
#     pinSend_sleep()
#     return

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
