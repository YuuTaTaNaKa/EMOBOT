# 感情の読み取りと感情スコア生成を行う
# from gpiozero import LED
from time import sleep
import requests
import RPi.GPIO as GPIO
import time



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
    calmness = emotion_scores.get("calmness", 0)
    anger = emotion_scores.get("anger", 0)
    sadness = emotion_scores.get("sadness", 0)
    joy = emotion_scores.get("joy", 0)
    energy = emotion_scores.get("energy", 0)

    # 表情を決定
    selected_emotion = determine_emotion(calmness, anger, sadness, joy, energy)

    # 結果を表示
    print(f"\n選択された表情: {selected_emotion}")

    # OutSoundに送信（コメント解除して使用）
    # raspi4_send(selected_emotion)

# ラズパイ4へ表情データを送信（GPIOなどを用いる場合）
def raspi4_send(emotion):
    print(f"ラズパイ4へ '{emotion}' を送信")
    # ここで GPIO制御や通信処理を実装

    # raspi4_send(strongest_emotion)


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