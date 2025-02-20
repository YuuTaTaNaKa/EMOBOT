# 感情の読み取りと感情スコア生成を行う
# from gpiozero import LED
from time import sleep
import requests
# import RPi.GPIO as GPIO
import time
import os
import pygame

# GPIO.setmode(GPIO.BCM)
# GPIO.setup(23, GPIO.OUT)
# GPIO.setup(24, GPIO.OUT)
# GPIO.setup(25, GPIO.OUT)
# GPIO.setup(8, GPIO.OUT)
# GPIO.setup(7, GPIO.OUT)
# GPIO.setup(1, GPIO.OUT)
# GPIO.setup(12, GPIO.OUT)
# GPIO.setup(16, GPIO.OUT)
# GPIO.setup(20, GPIO.OUT)
# GPIO.setup(19, GPIO.OUT)
# GPIO.setup(13, GPIO.OUT)
# GPIO.setup(6, GPIO.OUT)
# GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# GPIO.setup(0, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# GPIO.setup(9, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
current_process = "sleep"

#「あかりん音声ファイルパス」

anger_mp3 = os.path.join(os.path.dirname(__file__), "..", "se", "anger.mp3")
doubt_mp3 = os.path.join(os.path.dirname(__file__), "..", "se", "doubt.mp3")
embarrassed_mp3 = os.path.join(os.path.dirname(__file__), "..", "se", "embarrassed.mp3")
kirarin_mp3 = os.path.join(os.path.dirname(__file__), "..", "se", "kirarin.mp3")
omg_mp3 = os.path.join(os.path.dirname(__file__), "..", "se", "omg.mp3")
sad_mp3 = os.path.join(os.path.dirname(__file__), "..", "se", "sad.mp3")
smile_mp3 = os.path.join(os.path.dirname(__file__), "..", "se", "smile.mp3")
testsound_scream_mp3 = os.path.join(os.path.dirname(__file__), "..", "se", "testsound_scream.mp3")


def empath(voice):
    url = "https://api.webempath.net/v2/analyzeWav"
    api_key = "-m_gBMbIiYjyyA-3k6ahRpM9X14-zg6gTg3HqokktI4"

    # ファイルをアップロード
    with open(voice, "rb") as audio_file:
        files = {"wav": audio_file}
        data = {"apikey": api_key}
        response = requests.post(url, files=files, data=data)

    # レスポンスを処理
    if response.status_code == 200:
        print(response.json())  # レスポンスがJSONの場合
        emotion(response.json())
    else:
        print(f"HTTP status {response.status_code}")
        emotion(f"HTTP status {response.status_code}")

# 感情スコアをもとに表情を決定する
def determine_emotion(calmness, anger, sadness, joy, energy):
    if 20 <= calmness <= 50:
        return "thinEye"
    if 20 <= anger <= 50:
        return "anger"
    if 20 <= sadness <= 50:
        return "sad"
    if 25 <= joy <= 50 and 25 <= energy <= 50:
        return "kirarin"
    if 15 <= joy <= 20:
        return "embarrassed"
    if 15 <= energy <= 25:
        return "smile"
    
    return "doubt"  # どの条件にも当てはまらない場合

# 感情スコアの仕分けと最も強い感情の決定
def emotion(scores):
    # APIの返却データ（感情スコア）
    emotion_scores = scores

    # 各感情のスコアを取得（データがない場合のデフォルト値は0）
    calm = emotion_scores.get("calmness", 0)
    anger = emotion_scores.get("anger", 0)
    sad = emotion_scores.get("sadness", 0)
    joy = emotion_scores.get("joy", 0)
    energy = emotion_scores.get("energy", 0)

    # 表情を決定
    selected_emotion = determine_emotion(calm, anger, sad, joy, energy)

    # 結果を表示
    print(f"\n選択された表情: {selected_emotion}")

    def pinSend(pin):
        # GPIO.output(pin, GPIO.HIGH)
        time.sleep(3)
        # GPIO.output(pin, GPIO.LOW)

    if selected_emotion ==calm:
        pinSend(20)
        pygame.mixer.init()
        pygame.mixer.music.load(smile_mp3)
        pygame.mixer.music.play(0)
    elif selected_emotion == anger:
        pinSend(6)
        pygame.mixer.init()
        pygame.mixer.music.load(anger_mp3)
        pygame.mixer.music.play(0)
    elif selected_emotion == sad:
        pinSend(12)
        pygame.mixer.init()
        pygame.mixer.music.load(sad_mp3)
        pygame.mixer.music.play(0)
    elif selected_emotion == joy:
        pinSend(8)
        pygame.mixer.init()
        pygame.mixer.music.load(kirarin_mp3)
        pygame.mixer.music.play(0)
    elif selected_emotion == energy:
        pinSend(7)
        pygame.mixer.init()
        pygame.mixer.music.load(smile_mp3)
        pygame.mixer.music.play(0)
    else:
        pinSend(13)
        pygame.mixer.init()
        pygame.mixer.music.load(doubt_mp3)
        pygame.mixer.music.play(0)


#一番高い値の感情を元に、Displayに信号を送る gpiozero
# def raspi4_send(strongest_emotion):
    
#     if strongest_emotion == "calm":
#         LED(17).on() 
#         pin = "LED(17)"
#     elif strongest_emotion == "anger":
#         LED(27).on()
#         pin = "LED(27)"
#     elif strongest_emotion == "joy":
#         LED(22).on()
#         pin = "LED(22)"
#     elif strongest_emotion == "sorrow":
#         LED(5).on()
#         pin = "LED(5)"
#     elif strongest_emotion == "energy":
#         LED(6).on()
#         pin = "LED(6)"

#     print(strongest_emotion + pin + "をONにします。")
#     sleep(3)


# 使用例
# empath("path_to_your_audio_file.wav")

"""
エモボットスコア

最大値５０ 最低値０

冷静さ、怒り、悲しみ、喜び、活気

thinEye
冷静さ２０～５０

anger
怒り２０～５０

sad
悲しみ２０～５０

kirarin
喜び２５～５０
活気２５～５０

embarrassed
喜び１５～２０

smile
活気１５～２５

"""