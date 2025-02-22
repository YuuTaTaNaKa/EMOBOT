# 感情の読み取りと感情スコア生成を行う
# from gpiozero import LED
from time import sleep
import requests
import RPi.GPIO as GPIO
import time
import os
import pygame
import OutSound

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
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(0, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(9, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
current_process = "sleep"

#「あかりん音声ファイルパス」

anger_mp3 = os.path.join(os.path.dirname(__file__), "..", "se", "anger_Pitch Changer.mp3")
doubt_mp3 = os.path.join(os.path.dirname(__file__), "..", "se", "doubt_Pitch Changer.mp3")
embarrassed_mp3 = os.path.join(os.path.dirname(__file__), "..", "se", "embarrassed_Pitch Changer.mp3")
kirarin_mp3 = os.path.join(os.path.dirname(__file__), "..", "se", "kirarin_Pitch Changer.mp3")
omg_mp3 = os.path.join(os.path.dirname(__file__), "..", "se", "omg_Pitch Changer.mp3")
sad_mp3 = os.path.join(os.path.dirname(__file__), "..", "se", "sad_Pitch Changer.mp3")
smile_mp3 = os.path.join(os.path.dirname(__file__), "..", "se", "smile_Pitch Changer.mp3")
testsound_scream_mp3 = os.path.join(os.path.dirname(__file__), "..", "se", "testsound_scream.mp3")


def empath(voice):
    url = "https://api.webempath.net/v2/analyzeWav"
    api_key = "S-WexRCCl-JrmrSHoQY3il76YXx5KcKG478CX0Ddrjc"

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
    emotions = {
        "calmness": calmness,
        "anger": anger,
        "sadness": sadness,
        "joy": joy,
        "energy": energy
    }

    # スコアが高い順にソート
    sorted_emotions = sorted(emotions.items(), key=lambda x: x[1], reverse=True)
    
    # 上位1位と2位の感情を取得
    top_emotion, top_score = sorted_emotions[0]  # 1位
    second_emotion, second_score = sorted_emotions[1]  # 2位

    # **1位の感情が圧倒的に高い場合**（50以上なら単独で判断）
    if top_score >= 50:
        return map_emotion_to_expression(top_emotion)

    # **1位と2位の組み合わせで表情を決定**
    return determine_combined_expression(top_emotion, second_emotion, top_score, second_score)


def map_emotion_to_expression(emotion):
    """各感情を直接表情にマッピング"""
    mapping = {
        "calmness": "thinEye",
        "anger": "anger",
        "sadness": "sad",
        "joy": "smile",
        "energy": "kirarin"
    }
    return mapping.get(emotion, "doubt")


def determine_combined_expression(emotion1, emotion2, score1, score2):
    """上位2つの感情スコアを考慮して表情を決定"""

    # 喜び + 活力 → "kirarin"
    if "joy" in {emotion1, emotion2} and "energy" in {emotion1, emotion2}:
        return "kirarin"

    # 喜び + 少しの活力 → "smile"
    if emotion1 == "joy" and score1 >= 25 and emotion2 == "energy" and score2 >= 15:
        return "smile"

    # 喜び + 少しの恥ずかしさ → "embarrassed"
    if emotion1 == "joy" and 15 <= score1 < 25:
        return "embarrassed"

    # 落ち着きが高い場合は "thinEye"
    if emotion1 == "calmness" and score1 >= 20:
        return "thinEye"

    # 怒りが少し強い場合 → "anger"
    if emotion1 == "anger" and score1 >= 20:
        return "anger"

    # 悲しみが少し強い場合 → "sad"
    if emotion1 == "sadness" and score1 >= 20:
        return "sad"

    # どの条件にも当てはまらない場合 → "doubt"
    return "doubt"



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
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(3)
        GPIO.output(pin, GPIO.LOW)

    if selected_emotion == "thinEye":
        pinSend(20)
        OutSound.voice_smile
    elif selected_emotion == "anger":
        pinSend(6)
        OutSound.voice_anger()
    elif selected_emotion == "sad":
        pinSend(12)
        OutSound.voice_sad()
    elif selected_emotion == "smile":
        pinSend(8)
        OutSound.voice_smile()
    elif selected_emotion == "kirarin":
        pinSend(7)
        OutSound.voice_kirarin()
    else:
        pinSend(13)
        OutSound.voice_doubt()



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