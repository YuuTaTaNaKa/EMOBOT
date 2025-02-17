import RPi.GPIO as GPIO
import time

# GPIO設定
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# 使用するピン（1本だけ）
PIN = 23

# ピンを出力に設定
GPIO.setup(PIN, GPIO.OUT)

# 5秒間 HIGH（ON）にする
GPIO.output(PIN, GPIO.HIGH)
print(f"GPIO {PIN} → HIGH（送信）")
time.sleep(5)

# LOW（OFF）に戻す
GPIO.output(PIN, GPIO.LOW)
print(f"GPIO {PIN} → LOW（送信終了）")

# GPIOクリーンアップ
GPIO.cleanup()
