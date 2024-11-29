# ラズパイ上でインストールするライブラリ
# import gpiozero as LED
import time

# 通常時（寝てるとき）
def led_sleep():
    print("青色に光る")

# コマンドを受け付けるとき
def led_accept():
    print("緑色に光る")

# コマンドを実行しているとき
def led_execution():
    print("黄色に光る")

# エラーが発生したとき
def led_error():
    print("赤色に光る")

#音楽を再生しているとき
def led_music():
    print("紫色に光る")
