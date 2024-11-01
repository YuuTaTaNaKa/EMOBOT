# 音声入力をもとに処理を行うスレッド
import time
import OutSound
import EarProcess
import DisplayProcess

def proces(command):
    print("音声入力をもとに処理を行います")

    if "おはよう" in command:
        print("おはよう")