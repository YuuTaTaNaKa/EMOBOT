# 耳の処理を行うスレッド
import RPi.GPIO as GPIO
import time

servo_pin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

pwm = GPIO.PWM(servo_pin, 50)
pwm.start(0)

def set_angle(angle):
    duty = (angle / 18) + 2.5
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.5)
    pwm.ChangeDutyCycle(0)

def earMove():
    print("耳の処理を行います。")
    set_angle(0)
    time.sleep(1)
    set_angle(120)
    time.sleep(1)
    set_angle(40)
    time.sleep(1)
    set_angle(0)
    time.sleep(1)
    return
