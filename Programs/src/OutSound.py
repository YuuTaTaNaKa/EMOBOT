# 音声出力スレッド
import time
from playsound import playsound
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
Musics = [os.path.join(os.path.dirname(__file__), "..", "se", "167.mp3"), ""]

# -------------------------------〈メソッド〉--------------------------------


#「挨拶」*************************************************************   

def greet_morning():
    playsound(smile_mp3)
    #print("おはよう")
    return

def greet_afternoon():
    playsound(smile_mp3)
    #print("こんにちは")
    return

def greet_night():
    playsound(smile_mp3)
    #print("こんばんは")
    return

def bye():
    playsound(smile_mp3)
    #print("さようなら")
    return

def im_going():
    playsound(smile_mp3)
    #print("いってきます")
    return

def welcome_home():
    playsound(smile_mp3)
    #print("おかえりなさい")
    return

def good_night():
    playsound(smile_mp3)
    #print("おやすみ")
    return

#「感情」************************************************************* 

def happy():
    playsound(smile_mp3)
    # print("うれしい")
    return

def sad():
    playsound(sad_mp3)
    # print("悲しい")
    return

def surprise():
    playsound(omg_mp3)
    # print("驚き")
    return

def fear():
    playsound(omg_mp3)
    # print("恐れ")
    return

#「利用者からの返事」*************************************************************  

def no():
    playsound(doubt_mp3)
    # print("わかりません")
    return

def ok():
    playsound(doubt_mp3)
    # print("わかりました")
    return

#「Music」*************************************************************  

def playMusic():
    playsound(choice(Musics))
    # print("音楽を再生します")
    return

# 汎用処理
def stop():
    # print("停止")
    return

