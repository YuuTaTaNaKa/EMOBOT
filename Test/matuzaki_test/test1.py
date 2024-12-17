import speech_recognition as sr
import pyttsx3
import requests

# 音声認識の初期化
recognizer = sr.Recognizer()

# 音声出力の初期化
engine = pyttsx3.init()

# ユーザープロファイル
user_profile = {
    "name": "しげる",
    "city": "松﨑"
}

# 音声出力関数
def speak(text):
    engine.say(text)
    engine.runAndWait()  # ここで音声の再生が終わるまで待機する

# 音声認識関数
def listen():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("何か話してください...")
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio, language='ja-JP')
            print(f"認識されたコマンド: {command}")
            return command
        except sr.UnknownValueError:
            speak("音声が理解できませんでした。もう一度お話しください。")
        except sr.RequestError as e:
            speak(f"音声認識サービスに接続できませんでした。詳細: {e}")

# 天気情報取得関数
def get_weather():
    city = user_profile['city']
    api_key = "your_openweathermap_api_key"  # OpenWeatherMapのAPIキーを入力
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        tenki_data = requests.get(url).json()
        
        if tenki_data.get("cod") != 200:
            # OpenWeatherMap APIのエラー処理
            error_message = tenki_data.get("message", "不明なエラーが発生しました。")
            speak(f"天気情報の取得に失敗しました: {error_message}")
            return
        
        weather_description = tenki_data["weather"][0]["description"]
        temperature = tenki_data["main"]["temp"]
        speak(f"{city}の天気は、{weather_description}、気温は{temperature}度です。")
    except requests.exceptions.RequestException as e:
        speak(f"天気情報の取得中に接続エラーが発生しました: {e}")
    except ValueError as e:
        speak(f"天気情報の処理中にエラーが発生しました: {e}")

# ユーザーに挨拶
def greet_user():
    speak(f"こんにちは、{user_profile['name']}さん。何をお手伝いできますか？")

# 音声アシスタントのループ処理
def assistant():
    greet_user()  # プログラム起動時に挨拶

    while True:
        command = listen()

        if command:
            if "終了" in command:
                speak("さようなら")
                break
            elif "天気" in command:
                speak("現在の天気を調べます...")
                get_weather()
            elif "時間" in command:
                from datetime import datetime
                current_time = datetime.now().strftime("%H時%M分です")
                speak(f"今の時間は {current_time}")
            else:
                speak("すみません、そのコマンドは理解できませんでした。")

# アシスタントの起動
assistant()