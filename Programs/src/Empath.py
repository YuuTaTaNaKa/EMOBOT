# 感情の読み取りを行います
import time
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
    else:
        print(f"HTTP status {response.status_code}")

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

smile
喜び１５～２５
活気１５～２５

"""