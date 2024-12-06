import pyaudio
import numpy as np

# マイクの設定
FORMAT = pyaudio.paInt16  # 音声のフォーマット
CHANNELS = 1  # モノラル
RATE = 44100  # サンプリングレート（44.1kHz）
CHUNK = 1024  # チャンクサイズ（音声の一度に取得するデータ量）
THRESHOLD = 500  # 音の閾値（これより大きい音は「音あり」と判定）

# PyAudioのインスタンスを作成
p = pyaudio.PyAudio()

# マイクのストリームを開く
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("音をチェックしています...")

try:
    while True:
        # 音声データをチャンク単位で取得
        data = np.frombuffer(stream.read(CHUNK), dtype=np.int16)
        
        # 音量の平均を計算
        volume = np.linalg.norm(data)  # 音量を計算（L2ノルム）
        
        # 音量が閾値を超えていれば「音あり」
        if volume > THRESHOLD:
            print("音あり！")
        else:
            print("音なし...")
        
except KeyboardInterrupt:
    print("終了します")

finally:
    stream.stop_stream()
    stream.close()
    p.terminate()
