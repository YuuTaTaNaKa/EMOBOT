import RPi.GPIO as GPIO
import time

# GPIO設定
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# 使用するピン（1本だけ）
PIN = 23

# ピンを入力に設定
GPIO.setup(PIN, GPIO.IN)

print("GPIO 23 の信号を待機中...")

while True:
    if GPIO.input(PIN) == GPIO.HIGH:
        print("GPIO 23 → HIGH（受信）")
    else:
        print("GPIO 23 → LOW（待機）")
    
    time.sleep(1)  # 1秒ごとにチェック
