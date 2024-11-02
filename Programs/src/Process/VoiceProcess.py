# 音声入力をもとに処理を行うスレッド
import time
import OutSound
import EarProcess
import DisplayProcess

def proces(command):
    print("音声入力をもとに処理を行います")

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
    elif "おやすみ" in command:
        print("おやすみ")
        OutSound.goodnight()
    elif "音楽を再生します" in command:
        print("音楽を再生します")
        OutSound.playMusic()
    elif "わかりました" in command:
        print("わかりました")
        OutSound.OK()
    elif "わかりません" in command:
        print("わかりません")
        OutSound.NO()
    else:
        print("なんて言ったかわかんないなぁ")