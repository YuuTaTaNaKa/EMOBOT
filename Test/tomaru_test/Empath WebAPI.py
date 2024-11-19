
#python3.11.9で使用できるコード、chatGPT引用
import requests

# APIエンドポイント
url = "https://api.webempath.net/v2/analyzeWav"

# APIキー
api_key = "-m_gBMbIiYjyyA-3k6ahRpM9X14-zg6gTg3HqokktI4"

# 音声ファイルのパス
wav_file_path = "/PATH/TO/WAVFILE.wav"

# リクエストのデータ
files = {
    'apikey': (None, api_key),
    'wav': open(wav_file_path, 'rb')
}

# リクエストを送信
response = requests.post(url, files=files)

# レスポンスの確認
if response.status_code == 200:
    print(response.json())  # 結果をJSONで表示
else:
    print(f"HTTP status {response.status_code}")


# pip install poster==0.8.1


#仕様書のデータ

# from poster.encode import multipart_encode, MultipartParam
# from poster.streaminghttp import register_openers
# import urllib2

# url="https://api.webempath.net/v2/analyzeWav"
# register_openers()
# items = []
# items.append(MultipartParam('apikey', "YOUR_APIKEY"))
# items.append(MultipartParam.from_file('wav', "/PATH/TO/WAVFILE.wav"))
# datagen, headers = multipart_encode(items)
# request = urllib2.Request(url, datagen, headers)
# response = urllib2.urlopen(request)
# if response.getcode() == 200:
#     print(response.read())
# else:
#     print("HTTP status %d" % (response.getcode()))