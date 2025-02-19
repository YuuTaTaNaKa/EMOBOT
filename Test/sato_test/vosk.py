import json
import pyaudio
from vosk import Model, KaldiRecognizer

# 日本語モデルのパス
MODEL_PATH = "vosk-model-ja-0.22"

# モデルを読み込む
model = Model(MODEL_PATH)
recognizer = KaldiRecognizer(model, 16000)

# マイク設定
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

print("話してください（Ctrl+Cで終了）...")

try:
    while True:
        data = stream.read(4000, exception_on_overflow=False)
        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            print("認識結果:", result["text"])
except KeyboardInterrupt:
    print("終了します。")
    stream.stop_stream()
    stream.close()
    p.terminate()
