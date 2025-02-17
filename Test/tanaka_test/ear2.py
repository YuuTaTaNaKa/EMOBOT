import RPi.GPIO as GPIO
import time

servo_pin = 18  # サーボを接続する GPIO 番号

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

pwm = GPIO.PWM(servo_pin, 50)  # 50Hz の PWM を生成
pwm.start(0)

def set_angle(angle):
    duty = (angle / 18) + 2.5  # 角度を PWM のデューティ比に変換
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.5)
    pwm.ChangeDutyCycle(0)  # 信号を止めて振動を防ぐ

try:
    set_angle(0)   # 0度
    time.sleep(1)
    set_angle(90)  # 90度
    time.sleep(1)
    set_angle(180) # 180度
    time.sleep(1)
finally:
    pwm.stop()
    GPIO.cleanup()
