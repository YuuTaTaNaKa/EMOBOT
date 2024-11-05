# 音声出力スレッド
import time
from playsound import playsound
Angry = []
Happy = []
Sad = []
Surprise = []
Fear = []
Greet_morning = []
Greet_afternoon = []
Greet_night = []
Goodnight = []
Bye = []
Ok = []
No = []
Musics = []

# 感情
def angry():
    print("EMOBOTだよ！")
    return

def happy():
    print("うれしい")
    return

def sad():
    print("悲しい")
    return

def surprise():
    print("驚き")
    return

def fear():
    print("恐れ")
    return


# 挨拶
def greet_morning():
    print("おはよう")
    return

def greet_afternoon():
    print("こんにちは")
    return

def greet_night():
    print("こんばんは")
    return

def goodnight():
    print("おやすみ")
    return

def bye():
    print("さようなら")
    return

# 
def no():
    print("わかりません")
    return

def ok():
    print("わかりました")
    return

# 音楽の再生
def playMusic():
    print("音楽を再生します")
    return


# 汎用処理
def stop():
    print("停止")
    return

