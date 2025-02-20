# 音声入力をもとに処理を行うスレッド
import time
import OutSound
import Empath
import InVoice
import Display
import OutSound
import subprocess
import RPi.GPIO as GPIO
# import LED
# import gpiozero
import EarProcess

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(1, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(0, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(9, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
current_process = "sleep"

def assistant():
    global current_process
    print("0")

    print("エモボットと呼びかけてください")
    
    while True:
        print("1")
        print(current_process)
        # エムボットが呼ばれるまで待機
        command, _ = InVoice.listen(mic_timeout=5, phrase_time_limit=5, number=0)
        # 「エムボット」と認識したら起動
        emobot_keywords = ["エモボット", "エムボット", "えもぼっと", "EMOBOT", "emobot"]

        # if GPIO.input(5, GPIO.HIGH):
        #     current_process = "accept"

        # if current_process == "sleep":
        print("2")
        print(current_process)
        if command and any(word in command for word in emobot_keywords):
            print("エモボット起動！ 感情分析モードへ移行します")
            current_process = "accept"
            GPIO.output(25, GPIO.LOW)
            GPIO.output(23, GPIO.HIGH)
            print("3")
        else:
            print("?")
            continue
        
        while True:
            print("4")
            print(current_process)
            # ユーザーの問いかけを取得
            order, audio_file = InVoice.listen(mic_timeout=5, phrase_time_limit=5, number=1)

            if order:
                current_process = "execution"
                GPIO.output(23, GPIO.LOW)
                GPIO.output(24, GPIO.HIGH)
                print(f"認識したコマンド: {order}")

                # 「おやすみ」と言われたらエモボットを停止し、待機状態に戻る
                if "おやすみ" in order:
                    print("スリープモードに移行します...")
                    current_process = "sleep"
                    GPIO.output(24, GPIO.LOW)
                    GPIO.output(25, GPIO.HIGH)
                    break  # 内部ループを抜け、エモボット待機状態に戻る
                # 特定のコマンドが含まれている場合、感情分析は実行せず、コマンド処理を行う
                elif process(order):
                    print(f"コマンド {order} の処理を実行しました")
                    current_process = "sleep"
                    break
                else:
                    # コマンドが含まれていなかった場合、感情分析を実行
                    if audio_file:
                        print("感情分析を実行します...")
                        empath_transfer(audio_file)
                        break
                
                # 音声入力を再度待機
                continue
            else:
                print("なんて言ったかわかんないなぁ")
                continue  # 再度音声入力を待機するためにループ

        

"""
pin
mein  disp  動作するもの
23    23    acceptの受け取り
24    24    executionの受け取り
25    25    sleepの受け取り
 8     8    smileの受け取り
 7     7    kirarinの受け取り
 1     1    embarrassedの受け取り
12    12    sadの受け取り
16    16    winkの受け取り
20    20    thinEyeの受け取り
19    19    omgの受け取り
13    13    doubtの受け取り
 6     6    angerの受け取り
 5     5    sleep時に画面タッチしたときに信号を出力
 0     0    accept時に画面タッチしたときに信号を出力
11     9
"""

def process(command):
    print("音声入力をもとに処理を行います")
    startMusic_keywords = ["おんがくをながして","音楽を流して","おんがくを流して","音楽をながして"] 
    stopMusic_keywords = ["おんがくをとめて","音楽を止めて","おんがくを止めて","音楽をとめて"]


    def pinSend(pin):
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(3)
        GPIO.output(pin, GPIO.LOW)
        return

    #　「あいさつ」　*************************************************************   

    if "おはよう" in command: 
        print("おはよう")
        # Display.face_smile()
        pinSend(8)
        EarProcess.earMove()
        OutSound.greet_morning()

    elif "こんにちは" in command:
        print("こんにちは")
        # Display.face_smile()
        pinSend(8)
        EarProcess.earMove()
        OutSound.greet_afternoon()

    elif "こんばんは" in command:
        print("こんばんは")
        # Display.face_smile()
        pinSend(8)
        EarProcess.earMove()
        OutSound.greet_night()

    elif "さようなら" in command:
        print("さようなら")
        # Display.face_smile()
        pinSend(8)
        EarProcess.earMove()
        OutSound.bye()
    
    elif "いってきます" in command:
        print("いってきます")
        # Display.face_smile()
        pinSend(8)
        EarProcess.earMove()
        OutSound.im_going()

    elif "おかえりなさい" in command:
        print("おかえりなさい")
        # Display.face_smile()
        pinSend(8)
        EarProcess.earMove()
        OutSound.welcome_home()

    elif "おやすみ" in command:
        # Display.face_sleep()
        pinSend(25)
        EarProcess.earMove()
        OutSound.good_night()


#　「機能」　*************************************************************  

    elif command and any(word in command for word in startMusic_keywords):
        print("音楽を再生します")
        # LED.led_music()
        pinSend(7)
        OutSound.playMusic()
        
    elif command and any(word in command for word in stopMusic_keywords):
        OutSound.stopMusic()

    elif "シャットダウン" in command:
        print("シャットダウン")
        ComandShutdown = "shutdown now"
        result = subprocess.run(ComandShutdown, shell=True, text=True, capture_output=True)
        print(result.stdout)

    elif "再起動" in command:
        print("再起動")
        ComandReboot = "reboot"
        result = subprocess.run(ComandReboot, shell=True, text=True, capture_output=True)
        print(result.stdout)

    # elif "クイズ" in command:
    #     print("クイズを出して")
    #     DisplayProcess.quiz()
    #     #OutSound() ??

    else:
        print("コマンドに含まれてはいません")
        return False

# ********************************〔Empath.pyの呼び出し〕*******************************************
def empath_transfer(audio_file):
    if not audio_file:
        print("音声データがありません。")
        return
    
    # 感情分析
    print("感情を分析しています...")
    Empath.empath(audio_file)
    
# #キーワードコマンド

#     elif "いいね" in command:
#         print("いいね")
#         # Display.face_embarrassed()
#         OutSound.welcome_home()

#     elif "体調が悪い" in command:
#         print("体調が悪い")
#         # Display.face_sad()
#         OutSound.welcome_home()

#     elif "体調がいい" in command:
#         print("体調がいい")
#         # Display.face_smile()
#         OutSound.welcome_home()

#     elif "誕生日" in command:
#         print("誕生日")
#         # Display.face_kirarin()
#         OutSound.welcome_home()

#     elif "ハッピーバースデー" in command:
#         print("ハッピーバースデー")
#         # Display.face_kirarin()
#         OutSound.welcome_home()

#     elif "いい気分" in command:
#         print("いい気分")
#         # Display.face_smile()
#         OutSound.welcome_home()

#     elif "かっこいい" in command:
#         print("かっこいい")
#         # Display.face_wink()
#         OutSound.welcome_home()

#     elif "癒してほしい" in command:
#         print("癒してほしい")
#         # Display.face_wink()
#         OutSound.playMusic()
#         # OutSound.welcome_home()

#     elif "つらい" in command:
#         print("つらい")
#         # Display.face_sad()
#         OutSound.welcome_home()

#     elif "疲れた" in command:
#         print("疲れた")
#         # Display.face_thinEye()
#         OutSound.welcome_home()

#     elif "しんどい" in command:
#         print("しんどい")
#         # Display.face_sad()
#         OutSound.welcome_home()

#     elif "おめでとう" in command:
#         print("おめでとう")
#         # Display.face_embarrassed()
#         OutSound.welcome_home()

#     elif "最高" in command:
#         print("最高")
#         # Display.face_kirarin()
#         OutSound.welcome_home()

#     elif "憂鬱" in command:
#         print("憂鬱")
#         # Display.face_sad()
#         OutSound.welcome_home()

# #　「感情」　*************************************************************       

#     elif "驚いた" in command:
#         print("驚いた")
#         # Display.face_smile()
#         OutSound.surprise()

#     elif "悲しい" in command:
#         print("悲しい")
#         # Display.face_sad()
#         OutSound.sad()

#     elif "こわい" in command:
#         print("こわい")
#         # Display.face_sad()
#         OutSound.fear()

#     elif "うれしい" in command:
#         print("うれしい")
#         # Display.face_embarrassed()
#         OutSound.happy()

#　「利用者からの返事」　*************************************************************  

    # elif "わかりました" in command:
    #     print("わかりました")
    #     # Display.face_embarrassed()
    #     OutSound.ok()

    # elif "わかりません" in command:
    #     print("わかりません")
    #     # Display.face_doubt()
    #     OutSound.no()
