from gpiozero import LED
from time import sleep

# LEDのグローバル変数
red_color = None
blue_color = None
green_color = None

# LEDをセットアップ
def setup_leds():
    global red_color, blue_color, green_color
    red_color = LED(17)
    blue_color = LED(27)
    green_color = LED(22)

# 通常時（寝ているとき）
def led_sleep():
    red_color.off()
    green_color.off()
    blue_color.on()

# コマンドを実行しているとき
def led_execution():
    red_color.off()
    blue_color.on()
    green_color.on()

# コマンドを受け付けるとき
def led_accept():
    red_color.off()
    blue_color.off()
    green_color.on()

# エラーが発生しているとき
def led_error():
    blue_color.off()
    green_color.off()
    red_color.on()

# 音楽を再生しているとき
def led_music():
    green_color.off()
    blue_color.on()
    red_color.on()

# 実行例
if __name__ == "__main__":
    setup_leds()  # LEDのセットアップ

    print("LED Sleep（通常時）")
    led_sleep()
    sleep(2)

    print("LED Execution（コマンド実行中）")
    led_execution()
    sleep(2)

    print("LED Accept（コマンド受付中）")
    led_accept()
    sleep(2)

    print("LED Error（エラー発生）")
    led_error()
    sleep(2)

    print("LED Music（音楽再生中）")
    led_music()
    sleep(2)