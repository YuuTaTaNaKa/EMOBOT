from gpiozero import LED
from time import sleep
#色のパターン
#blue_color(青)
#red_color(赤)
#green_color(緑)
#通常時(寝ているとき)

red_color = LED(17)
blue_color = LED(27)
green_color = LED(22)

def led_sleep():
    global red_color, blue_color, green_color
    red_color.off()
    blue_color.on()
    green_color.off()

# コマンドを実行しているとき
def led_execution():
    global red_color, blue_color, green_color
    red_color.off()
    blue_color.on()
    green_color.on()


# コマンドを受け付けるとき
def led_accept():
    global red_color, blue_color, green_color
    red_color.off()
    blue_color.off()
    green_color.on()

#エラーが発生しているとき
def led_error():
    global red_color, blue_color, green_color
    red_color.on()
    blue_color.off()
    green_color.off()

#音楽を再生しているとき
def led_music():
    global red_color, blue_color, green_color
    red_color.on()
    blue_color.on()
    green_color.off()

# # ラズパイ上でインストールするライブラリ
# # import gpiozero as LED
# import time

# # 通常時（寝てるとき）
# def led_sleep():
#     print("青色に光る")

# # コマンドを受け付けるとき
# def led_accept():
#     print("緑色に光る")

# # コマンドを実行しているとき
# def led_execution():
#     print("黄色に光る")

# # エラーが発生したとき
# def led_error():
#     print("赤色に光る")

# #音楽を再生しているとき
# def led_music():
#     print("紫色に光る")
