import pigpio
import time
import sys

SERVO_PIN = 18

# pigpioを初期化
pi = pigpio.pi()

# 初期化に失敗した場合の対策
if not pi.connected:
    print("Error: pigpioデーモンが起動していないか、接続できません。")
    sys.exit()  # プログラムを終了

# サーボモーターを特定の角度に設定する関数
def set_angle(angle):
    assert 0 <= angle <= 180, '角度は0から180の間でなければなりません'
    
    # 角度を500から2500のパルス幅にマッピングする
    pulse_width = (angle / 180) * (2500 - 500) + 500
    
    # パルス幅を設定してサーボを回転させる
    pi.set_servo_pulsewidth(SERVO_PIN, pulse_width)

# 使用例
try:
    while True:
        set_angle(90)  # サーボを90度に設定
        time.sleep(1)
        
        set_angle(0)  # サーボを0度に設定
        time.sleep(1)
        
        set_angle(90)  # サーボを90度に設定
        time.sleep(1)
        
        set_angle(180)  # サーボを180度に設定
        time.sleep(1)
except KeyboardInterrupt:
    print("プログラムを終了します。")
finally:
    # サーボを停止してリソースを解放
    pi.set_servo_pulsewidth(SERVO_PIN, 0)
    pi.stop()
