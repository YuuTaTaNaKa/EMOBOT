import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)  
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # プルダウン抵抗を有効化

while True:
    if GPIO.input(23) == GPIO.HIGH:
        print("HIGH detected!")
    else:
        print("LOW detected!")
    time.sleep(1)  # 1秒ごとに確認
