from pydub import AudioSegment
import speech_recognition as sr
# import Process.VoiceProcess_Empath as vp
import time
import atexit
from Process import Empath

recognizer = sr.Recognizer()

# 音声ファイルを 11025Hz に変換する関数
def convert_sample_rate(input_file, output_file, target_rate=11025):
    audio = AudioSegment.from_file(input_file)
    audio = audio.set_frame_rate(target_rate)
    audio.export(output_file, format="wav")
    print(f"音声ファイルを {target_rate}Hz に変換しました: {output_file}")
    
# 音声wavファイルを5秒間のファイルにトリミング
def trim_audio(file_path, max_duration=5):
    """音声ファイルを最大指定時間にトリミングする"""
    audio = AudioSegment.from_wav(file_path)
    if len(audio) > max_duration * 1000:  # ミリ秒単位
        audio = audio[:max_duration * 1000]
        audio.export(file_path, format="wav")
        print(f"音声ファイルを {max_duration} 秒にトリミングしました: {file_path}")

# 音声認識関数
def listen(mic_timeout, phrase_time_limit,number):
    start_time = time.time()  # 現在の時刻を取得
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("何かをはなして")
        
        while True:
            # 音声の検出（5秒でタイムアウト）
            if time.time() - start_time > mic_timeout and number == 0:
                print("時間が切れました。")
                return None, None
             # 以下修正点
            if time.time() - start_time > mic_timeout and number == 1:
                print("時間が切れました。")
                return None, None
            # 以上修正点
            try:
                audio = recognizer.listen(source, timeout=mic_timeout, phrase_time_limit=phrase_time_limit)

                temp_audio_file = "temp_audio.wav"
                with open(temp_audio_file, "wb") as f:
                    f.write(audio.get_wav_data())
                
                # サンプルレートを変換
                converted_audio_file = "converted_audio.wav"
                convert_sample_rate(temp_audio_file, converted_audio_file)
                #ファイルを5秒にトリミング
                print("トリミング中止")
                trim_audio(converted_audio_file, max_duration=5)

                # 音声認識を実行
                command = recognizer.recognize_google(audio, language='ja-JP')  # 日本語設定  
                print("テキスト変換完了")             
                return command,converted_audio_file
                #
                # ログファイルを開く
                logfile = open("alsa_log.txt", 'a')
                sys.stderr = logfile

                # プログラム終了時にファイルを閉じる
                atexit.register(logfile.close)
                #
            except sr.WaitTimeoutError:
                print("タイムアウトしました。音声入力が検出されませんでした。")
                continue  # 再度待機
            except sr.UnknownValueError:
                print("よくわからなかったな。もういっかい！")
            except sr.RequestError as e:
                print(f"うまくつながらないな: {e}")
                return None, None



# *************************************************************************************************
def stop():
    print("停止")
    return
