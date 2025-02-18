import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("音声を聞いています...")
    audio = r.listen(source)

try:
    print("認識結果: ", r.recognize_google(audio, language="ja-JP"))
except sr.UnknownValueError:
    print("音声を理解できませんでした")
except sr.RequestError as e:
    print(f"Google Speech API に接続できませんでした: {e}")
