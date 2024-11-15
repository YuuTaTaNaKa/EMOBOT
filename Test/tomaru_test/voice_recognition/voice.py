#!python3.11
import speech_recognition as sr

listener = sr.Recognizer()
try:
    with sr.Microphone() as source:
        print("Listening...")
        voice = listener.listen(source)
        voice_text = listener.recognize_google(voice, language="ja-JP")
        print(voice_text)
except:
    print('Sorry, I could not listen')

"""
使用するAPI(ターミナルでのインストール)
SpeechRecognitionのインストール
まずはSpeechRecognitionのライブラリをインストールします。

pip install SpeechRecognition

次に音声を録音・保存・再選する機能があるPyAudioをインストールします。

pip install PyAudio


"""