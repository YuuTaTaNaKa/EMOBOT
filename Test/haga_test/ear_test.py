import pigpio
import time

SERVO_PIN = 18

# pigpioを初期化
pi = pigpio.pi()

# サーボモーターを特定の角度に設定する関数
def set_angle(angle):
    assert 0 <= angle <= 180, '角度は0から180の間でなければなりません'
    
    # 角度を500から2500のパルス幅にマッピングする
    pulse_width = (angle / 180) * (2500 - 500) + 500
    
    # パルス幅を設定してサーボを回転させる
    pi.set_servo_pulsewidth(SERVO_PIN, pulse_width)

    #音声を受け取ろう！
    
# 使用例
while True:
    set_angle(90) # サーボを90度に設定
    time.sleep(1)
    
    set_angle(0) # サーボを0度に設定
    time.sleep(1)
    
    set_angle(90) # サーボを90度に設定
    time.sleep(1)
    
    set_angle(180) # サーボを180度に設定
    time.sleep(1)