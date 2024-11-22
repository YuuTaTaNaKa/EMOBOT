# 音声出力スレッド
import time
from playsound import playsound
import os
from random import choice

# -------------------------------〈配列〉--------------------------------

#「挨拶」*************************

#「おはよう」
Greet_morning = ["Programs/se/testsound_scream.mp3"]
#「こんにちは」
Greet_afternoon = []
#「こんばんわ」
Greet_night = []
#「さようなら、ばいばい」
Bye = []
#「いってきます」
Im_going = []
#「おかえり」
Welcome_home = []
#「おやすみ」
Good_night = []

#「感情」*************************

#「怒り」
Angry = []
#「幸せ」
Happy = []
#「悲しい」
Sad = []
#「驚き」
Surprise = []
#「恐れ」
Fear = []

#「返事」*************************

#「はい、」
yes = []

#「いいえ、だめ」
No = []

#「了解、オーケー」
Ok = []

#「機能」*************************

#「SpotifyAPI」
Musics = []
#音楽を再生するね！的な奴いる？
Musics_messege = []

# -------------------------------〈メソッド〉--------------------------------


#「挨拶」*************************************************************   

def greet_morning():
    playsound(choice(Greet_morning))
    #print("おはよう")
    return

def greet_afternoon():
    playsound(choice(Greet_afternoon))
    #print("こんにちは")
    return

def greet_night():
    playsound(choice(Greet_night))
    #print("こんばんは")
    return

def bye():
    playsound(choice(Bye))
    #print("さようなら")
    return

def im_going():
    playsound(choice(Im_going))
    #print("いってきます")
    return

def welcome_home():
    playsound(choice(Welcome_home))
    #print("おかえりなさい")
    return

def good_night():
    playsound(choice(Good_night))
    #print("おやすみ")
    return

#「感情」************************************************************* 

def happy():
    playsound(choice(Happy))
    # print("うれしい")
    return

def sad():
    playsound(choice(Sad))
    # print("悲しい")
    return

def surprise():
    playsound(choice(Surprise))
    # print("驚き")
    return

def fear():
    playsound(choice(Fear))
    # print("恐れ")
    return

#「利用者からの返事」*************************************************************  

def no():
    playsound(choice(No))
    # print("わかりません")
    return

def ok():
    playsound(choice(Ok))
    # print("わかりました")
    return

#「Spotify_Music」*************************************************************  

def playMusic():
    playsound(choice(Musics_messege))
    playsound(choice(Musics))
    # print("音楽を再生します")
    return

# 汎用処理
def stop():
    # print("停止")
    return

