# 感情の読み取りと感情スコア生成を行う
from gpiozero import LED
from time import sleep
import requests

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

#感情スコアの仕分け、一番高い値の感情を採用
def emotion(scores):
    emotion_scores = scores

    # 仕分けの基準を設定
    def categorize_emotion(score):
        if score <= 5:
            return '低'
        elif score <= 15:
            return '中'
        else:
            return '高'

    # 感情を仕分ける
    sorted_emotions = {emotion: categorize_emotion(score) for emotion, score in emotion_scores.items() if emotion != 'error'}

    # 最も強い感情を選ぶ
    strongest_emotion = max(emotion_scores, key=emotion_scores.get)
    strongest_score = emotion_scores[strongest_emotion]

    # 結果を表示
    print("感情スコアの仕分け:")
    for emotion, category in sorted_emotions.items():
        print(f"{emotion}: {category}")

    print(f"\n最も強い感情は '{strongest_emotion}' で、スコアは {strongest_score} です。")
    raspi4_send(strongest_emotion)


#一番高い値の感情を元に、Displayに信号を送る gpiozero
def raspi4_send(strongest_emotion):
    
    if strongest_emotion == "calm":
        LED(17).on()
        pin = "LED(17)"
    elif strongest_emotion == "anger":
        LED(27).on()
        pin = "LED(27)"
    elif strongest_emotion == "joy":
        LED(22).on()
        pin = "LED(22)"
    elif strongest_emotion == "sorrow":
        LED(5).on()
        pin = "LED(5)"
    elif strongest_emotion == "energy":
        LED(6).on()
        pin = "LED(6)"

    print(strongest_emotion + pin + "をONにします。")
    sleep(3)
    LED.off
