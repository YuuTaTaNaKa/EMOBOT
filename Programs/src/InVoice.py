import speech_recognition as sr
import Process.VoiceProcess as vp
import time

recognizer = sr.Recognizer()

# 音声認識関数
def listen(timeout=8):
    start_time = time.time()  # 現在の時刻を取得
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("何かおはなしして")
        
        while True:
            # 音声の検出（5秒でタイムアウト）
            if time.time() - start_time > timeout:
                print("時間が切れました。")
                return None
            try:
                audio = recognizer.listen(source, timeout=5)
                command = recognizer.recognize_google(audio, language='ja-JP')  # 日本語設定
                print(f"認識されたコマンド: {command}")
                return command
            except sr.WaitTimeoutError:
                print("タイムアウトしました。音声入力が検出されませんでした。")
                continue  # 再度待機
            except sr.UnknownValueError:
                print("よくわからなかったな。もういっかい！")
            except sr.RequestError as e:
                print(f"うまくつながらないな: {e}")
                return None

# 音声アシスタントのループ処理
def assistant():
    print("なにをする？")
    while True:
        command = listen(timeout=8)
        
        if command is None:
            print("リセットされました。再度話しかけてください。")
            continue

        # エモボットに関連するキーワード
        emobot_keywords = ["エモボット", "エムボット", "えもぼっと", "EMOBOT", "emobot"]
        # 他のアシスタントのキーワード
        other_assistant_keywords = ["アレクサ", "あれくさ", "ALXA", "alxa", "オッケーグーグル", "おっけーぐーぐる", "OK Google", "ヘイシリー", "へいしり", "Hey Siri", "hey siri"]

        # エモボットのキーワードが含まれている場合
        if any(word in command for word in emobot_keywords):
            order = listen(timeout=8)  # 再度8秒間だけONにしてコマンドを聞き取る
            if order:
                vp.process(order)

        # 他のアシスタントのキーワードが含まれている場合
        elif any(word in command for word in other_assistant_keywords):
            vp.angry()
        
        # 想定外のキーワードの場合
        else:
            print("なんて言ったかわかんないなぁ")

def stop():
    print("停止")
    return