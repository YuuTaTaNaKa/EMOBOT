# 音声入力・感情認識用スレッド
import speech_recognition as sr
import Process.VoiceProcess as vp
import Process.Empath as ep
import time

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
        if "エモボット" or "えもぼっと" or "EMOBOT" or "emobot" in command:
            time.sleep(0.5)
            # 音声の出力
            # 音声の認識を実行
            order = listen()
            vp.process(order)
            ep.empath(order)
        if "アレクサ" or "あれくさ" or"ALXA"or "alxa" or "オッケーグーグル" or "おっけーぐーぐる" or "OK Google" or "ヘイシリー" or "へいしり" or "Hey Siri" or "hey siri" in command:
            time.sleep(0.5)
            vp.angry()
        else:
            print("なんて言ったかわかんないなぁ")

if __name__ == '__main__':
    assistant()