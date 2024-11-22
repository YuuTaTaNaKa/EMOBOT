# 音声入力をもとに処理を行うスレッド
import time

import OutSound
from Process import DisplayProcess
# import EarProcess

def process(command):
    print("音声入力をもとに処理を行います")

    #　「あいさつ」　*************************************************************   

    if "おはよう" in command:
        
        print("おはよう")
        OutSound.greet_morning()

    elif "こんにちは" in command:
        print("こんにちは")
        OutSound.greet_afternoon()

    elif "こんばんは" in command:
        print("こんばんは")
        OutSound.greet_night()

    elif "さようなら" in command:
        print("さようなら")
        OutSound.bye()
    
    elif "いってきます" in command:
        print("いってきます")
        OutSound.im_going()

    elif "おかえりなさい" in command:
        print("おかえりなさい")
        OutSound.welcome_home()

    elif "おやすみ" in command:
    #「目を閉じる」DisplayProcessに遷移
        DisplayProcess.close_eyes()
        OutSound.good_night()

#　「感情」　*************************************************************       

    elif "驚き" in command:
        print("驚き")
        OutSound.surprise()

    elif "悲しい" in command:
        print("悲しい")
        OutSound.sad()

    elif "恐れ" in command:
        print("恐れ")
        OutSound.fear()

    elif "うれしい" in command:
        print("うれしい")
        OutSound.happy()

#　「利用者からの返事」　*************************************************************  

    elif "わかりました" in command:
        print("わかりました")
        OutSound.ok()

    elif "わかりません" in command:
        print("わかりません")
        OutSound.no()

#　「機能」　*************************************************************  

    elif "音楽を再生して" in command:
        print("音楽を再生します")
        OutSound.playMusic()

    elif "クイズ" in command:
        print("クイズを出して")
        DisplayProcess.quiz()
        #OutSound() ??

    else:
        print("なんて言ったかわかんないなぁ")