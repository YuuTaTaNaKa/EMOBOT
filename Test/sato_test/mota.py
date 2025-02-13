import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)            # GPIOモード設定
servo_pin = 18                    # GPIOピン番号
GPIO.setup(servo_pin, GPIO.OUT)   # GPIO出力モード
pwm = GPIO.PWM(servo_pin, 50)     # 周波数50Hz
pwm.start(1.45)                   # パルス幅1.45ms＝ニュートラルポジション

try:
    while True:
        pwm.ChangeDutyCycle(12)   # パルス幅12msで、角度は約180度
        time.sleep(2)
        pwm.ChangeDutyCycle(2.5)  # パルス幅2.5msで、角度は約0度
        time.sleep(2)

except KeyboardInterrupt:
    # Ctrl+Cで終了（PWMを停止）
    pwm.stop()
