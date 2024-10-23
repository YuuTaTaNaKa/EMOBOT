# ラズパイ上でインストールするライブラリ
import gpiozero as LED
import time

# LEDのインスタンスを生成
led = 11
bule = 13
green = 15

led = LED.LED(led)