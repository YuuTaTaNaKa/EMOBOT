import warnings
from gpiozero import Servo
from time import sleep

# 警告を無視する
warnings.filterwarnings("ignore", category=UserWarning, module='gpiozero')

# サーボモーターの制御
servo = Servo(18)

servo.min()
sleep(1)

servo.mid()
sleep(1)

servo.max()
sleep(1)

# import pigpio
# import time
# import sys

# SERVO_PIN = 18

# # pigpioを初期化
# pi = pigpio.pi()

# # 初期化に失敗した場合の対策
# if not pi.connected:
#     print("Error: pigpioデーモンが起動していないか、接続できません。")
#     sys.exit()  # プログラムを終了

# # サーボモーターを特定の角度に設定する関数
# def set_angle(angle):
#     assert 0 <= angle <= 180, '角度は0から180の間でなければなりません'
    
#     # 角度を500から2500のパルス幅にマッピングする
#     pulse_width = (angle / 180) * (2500 - 500) + 500
    
#     # パルス幅を設定してサーボを回転させる
#     pi.set_servo_pulsewidth(SERVO_PIN, pulse_width)

# # 使用例
# try:
#     while True:
#         set_angle(90)  # サーボを90度に設定
#         time.sleep(1)
        
#         set_angle(0)  # サーボを0度に設定
#         time.sleep(1)
        
#         set_angle(90)  # サーボを90度に設定
#         time.sleep(1)
        
#         set_angle(180)  # サーボを180度に設定
#         time.sleep(1)
# except KeyboardInterrupt:
#     print("プログラムを終了します。")
# finally:
#     # サーボを停止してリソースを解放
#     pi.set_servo_pulsewidth(SERVO_PIN, 0)
#     pi.stop()

# import RPi.GPIO as GPIO
# import time

# # GPIOピンの設定
# IN1 = 17
# IN2 = 18
# ENA = 13  # PWM制御用

# GPIO.setmode(GPIO.BCM)
# GPIO.setup(IN1, GPIO.OUT)
# GPIO.setup(IN2, GPIO.OUT)
# GPIO.setup(ENA, GPIO.OUT)

# # PWM設定（50Hz, デューティ比0%から開始）
# pwm = GPIO.PWM(ENA, 50)
# pwm.start(0)

# def motor_forward(speed):
#     GPIO.output(IN1, GPIO.HIGH)
#     GPIO.output(IN2, GPIO.LOW)
#     pwm.ChangeDutyCycle(speed)

# def motor_backward(speed):
#     GPIO.output(IN1, GPIO.LOW)
#     GPIO.output(IN2, GPIO.HIGH)
#     pwm.ChangeDutyCycle(speed)

# def motor_stop():
#     GPIO.output(IN1, GPIO.LOW)
#     GPIO.output(IN2, GPIO.LOW)
#     pwm.ChangeDutyCycle(0)

# # モーターを動かす
# motor_forward(70)  # 70%の速度で前進
# time.sleep(3)      # 3秒間動作
# motor_stop()       # 停止

# # GPIOクリーンアップ
# pwm.stop()
# GPIO.cleanup()
