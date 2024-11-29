from pydub import AudioSegment
import speech_recognition as sr
import Process.VoiceProcess as vp
# import Process.VoiceProcess_Empath as vp
import time
from Process import Empath

recognizer = sr.Recognizer()

# 音声ファイルを 11025Hz に変換する関数
def convert_sample_rate(input_file, output_file, target_rate=11025):
    audio = AudioSegment.from_file(input_file)
    audio = audio.set_frame_rate(target_rate)
    audio.export(output_file, format="wav")
    print(f"音声ファイルを {target_rate}Hz に変換しました: {output_file}")

# 音声認識関数
def listen(timeout=8):
    start_time = time.time()  # 現在の時刻を取得
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("何かをはなして")
        
        while True:
            # 音声の検出（5秒でタイムアウト）
            if time.time() - start_time > timeout:
                print("時間が切れました。")
                return None, None
            try:
                audio = recognizer.listen(source, timeout=5)

                temp_audio_file = "temp_audio.wav"
                with open(temp_audio_file, "wb") as f:
                    f.write(audio.get_wav_data())
                
                # サンプルレートを変換
                converted_audio_file = "converted_audio.wav"
                convert_sample_rate(temp_audio_file, converted_audio_file)

                # 音声認識を実行
                command = recognizer.recognize_google(audio, language='ja-JP')  # 日本語設定
                print(f"認識されたコマンド: {command}")
                return command, converted_audio_file

            except sr.WaitTimeoutError:
                print("タイムアウトしました。音声入力が検出されませんでした。")
                continue  # 再度待機
            except sr.UnknownValueError:
                print("よくわからなかったな。もういっかい！")
            except sr.RequestError as e:
                print(f"うまくつながらないな: {e}")
                return None, None

# 音声アシスタントのループ処理
def assistant():
    print("なにをする？")
    while True:
        command, audio_file = listen(timeout=8)
        
        if command is None and audio_file is None:
            print("リセットされました。再度話しかけてください。")
            continue

        # エモボットに関連するキーワード
        emobot_keywords = ["エモボット", "エムボット", "えもぼっと", "EMOBOT", "emobot"]
        # 他のアシスタントのキーワード
        other_assistant_keywords = ["アレクサ", "あれくさ", "ALXA", "alxa", "オッケーグーグル", "おっけーぐーぐる", "OK Google", "ヘイシリー", "へいしり", "Hey Siri", "hey siri"]

        # エモボットのキーワードが含まれている場合
        if any(word in command for word in emobot_keywords):
            order = listen(timeout=8)[0]  # 再度8秒間だけONにしてコマンドを聞き取る
            if order:
                vp.process(order)

        # 他のアシスタントのキーワードが含まれている場合
        elif any(word in command for word in other_assistant_keywords):
            vp.angry()
        
        # 想定外のキーワードの場合
        else:
            empath_transfer(audio_file)
            print("なんて言ったかわかんないなぁ")


# ********************************〔Empath.pyの呼び出し〕*******************************************
def empath_transfer(audio_file):
    if not audio_file:
        print("音声データがありません。")
        return
    
    # 感情分析
    print("感情を分析しています...")
    Empath.empath(audio_file)

# *************************************************************************************************
def stop():
    print("停止")
    return
