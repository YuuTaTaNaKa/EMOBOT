# 音声入力・感情認識用スレッド
import speech_recognition as sr
import requests
from concurrent.futures import ThreadPoolExecutor
# 音声認識の初期化
recognizer = sr.Recognizer()

# 音声認識関数
def listen():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("何かおはなしして")
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio, language='ja-JP')  # 日本語設定
            print(f"認識されたコマンド: {command}")
            return command
        except sr.UnknownValueError:
            print("よくわからなかったな。もういっかい！")
        except sr.RequestError as e:
            print(f"うまくつながらないな: {e}")

# 音声アシスタントのループ処理
def assistant():
    print("なにをする？")
    while True:
        command = listen()

        if command:
            if "終了" in command:
                print("またね！")
                break
            elif "天気"in command:
                print("天気をしらべるね")
                # 天気情報を取得するコードを追加可能                
                def main():
                    api_key = "c9b6c535d058a8f1384591966dfd5492"  # OpenWeatherMapのAPIキーをここに入れる
                    city = "Gunma"  # 都市名
                    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

                    try:
                        tenki_data = requests.get(url).json()  # jsonで情報を取得
                    except requests.exceptions.RequestException as e:
                        print(f"調べるのに失敗しちゃった: {e}")
                        return
                    except ValueError as e:
                        print(f"結果が見れなかった。ごめんね: {e}")
                        return

                    print("------------------------")
                    print("都市名:", tenki_data["name"])
                    print("天気:", tenki_data["weather"][0]["description"])
                    print("気温 (摂氏):", tenki_data["main"]["temp"])
                    print("------------------------")

                if __name__ == '__main__':
                    main()


            elif "時間"in command:
                from datetime import datetime
                current_time = datetime.now().strftime("%H時%M分です")
                print(f"今の時間は {current_time}だよ")
            else:
                print("なんて言ったかわかんないなぁ")

"""
使用するAPI(ターミナルでのインストール)
pyttsx3 は、テキストを音声に変換できる Python ライブラリです。
そのため、テキストを提供すると、そのテキストが音声に変換されます。

pip install pyttsx3

OpenWeatherMapのAPIキー

c9b6c535d058a8f1384591966dfd5492

"""