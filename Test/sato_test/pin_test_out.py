import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)  # ピン番号の指定方法（BCM or BOARD）
GPIO.setup(23, GPIO.OUT,pull_up_down=GPIO.PUD_DOWN)  # ピン 23 を出力モードに設定

GPIO.output(23, GPIO.HIGH)  # ピンを HIGH にする
time.sleep(2)  # 2秒待機

GPIO.output(23, GPIO.LOW)  # ピンを LOW にする
time.sleep(2)

GPIO.cleanup()  # GPIO のリセット
