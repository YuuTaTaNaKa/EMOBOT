import speech_recognition as sr
import pyttsx3  # テキストを音声に変換するライブラリ

# 音声認識の初期化
recognizer = sr.Recognizer()

# 音声出力の初期化
engine = pyttsx3.init()

# 音声出力関数
def speak(text):
    engine.say(text)
    engine.runAndWait()

# 音声認識関数
def listen():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("何か話してください...")
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio, language='ja-JP')  # 日本語設定
            print(f"認識されたコマンド: {command}")
            return command
        except sr.UnknownValueError:
            speak("音声が理解できませんでした。もう一度お話しください。")
        except sr.RequestError as e:
            speak(f"音声認識サービスに接続できませんでした。詳細: {e}")

# 音声アシスタントのループ処理
def assistant():
    speak("こんにちは、何をお手伝いできますか？")
    while True:
        command = listen()

        if command:
            if "終了" in command:
                speak("さようなら")
                break
            # 喜び
            elif "" in command:
                speak()
            elif "" in command:
                speak()
            elif "" in command:
                speak()
            elif "" in command:
                speak()
            elif "" in command:
                speak()
            elif "" in command:
                speak()


            elif "天気"in command:
                speak("現在の天気を調べます...")
                # 天気情報を取得するコードを追加可能
            elif "時間"in command:
                from datetime import datetime
                current_time = datetime.now().strftime("%H時%M分です")
                speak(f"今の時間は {current_time}")
            else:
                speak("すみません、そのコマンドは理解できませんでした。")
            

# アシスタントの起動
assistant()

"""
使用するAPI(ターミナルでのインストール)
pyttsx3 は、テキストを音声に変換できる Python ライブラリです。
そのため、テキストを提供すると、そのテキストが音声に変換されます。

pip install pyttsx3

"""