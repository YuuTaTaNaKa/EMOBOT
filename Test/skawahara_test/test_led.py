from gpiozero import LED
from time import sleep
#色のパターン
#blue_color(青)
#red_color(赤)
#green_color(緑)
#通常時(寝ているとき)
def led_sleep():
    green_color = LED(22)
    red_color = LED(17)
    blue_color = LED(27)
    red_color.off()
    green_color.off()
    blue_color.on()


# コマンドを実行しているとき
def led_execution():
    red_color = LED(17)
    blue_color = LED(27)
    green_color = LED(22)
    red_color.off()
    blue_color.on()
    green_color.on()


# コマンドを受け付けるとき
def led_accept():
    red_color = LED(17)
    blue_color = LED(27)
    green_color = LED(22)
    red_color.off()
    blue_color.off()
    green_color.on()


#エラーが発生しているとき
def led_error():
    
    red_color = LED(17)
    blue_color = LED(27)
    green_color = LED(22)
    blue_color.off()
    green_color.off()
    red_color.on()


#音楽を再生しているとき
def led_music():
    red_color = LED(17)
    blue_color = LED(27)
    green_color = LED(22)
    green_color.off()
    blue_color.on()
    red_color.on()

led_execution()