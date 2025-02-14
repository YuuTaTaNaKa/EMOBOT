# 音声入力をもとに処理を行うスレッド
import time
import OutSound
import Empath
import InVoice
import Display
import subprocess
import RPi.GPIO as GPIO
# import LED
# import gpiozero
# import EarProcess

def assistant():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(23, GPIO.OUT)
    print("エムボットと呼びかけてください")
    
    while True:
        # エムボットが呼ばれるまで待機
        command, _ = InVoice.listen(mic_timeout=5, phrase_time_limit=5, number=0)

        # 「エムボット」と認識したら起動
        emobot_keywords = ["エモボット", "エムボット", "えもぼっと", "EMOBOT", "emobot"]
        if any(word in command for word in emobot_keywords):
            print("エモボット起動！ 感情分析モードへ移行します")
            GPIO.output(23, GPIO.HIGH)
            
            while True:
                # ユーザーの問いかけを取得
                order, audio_file = InVoice.listen(mic_timeout=5, phrase_time_limit=5, number=1)
                
                if order:
                    print(f"認識したコマンド: {order}")

                    # 「おやすみ」と言われたらエモボットを停止し、待機状態に戻る
                    if "おやすみ" in order:
                        print("スリープモードに移行します...")
                        break  # 内部ループを抜け、エモボット待機状態に戻る

                    # 特定のコマンドが含まれている場合、感情分析は実行せず、コマンド処理を行う
                    if process(order):
                        print(f"コマンド {order} の処理を実行しました")
                    else:
                        # コマンドが含まれていなかった場合、感情分析を実行
                        if audio_file:
                            print("感情分析を実行します...")
                            empath_transfer(audio_file)
                    
                    # 音声入力を再度待機
                    continue
                else:
                    print("なんて言ったかわかんないなぁ")
                    continue  # 再度音声入力を待機するためにループ

def process(command):
    print("音声入力をもとに処理を行います")

    #　「あいさつ」　*************************************************************   

    if "おはよう" in command: 
        print("おはよう")
        # Display.face_smile()
        OutSound.greet_morning()

    elif "こんにちは" in command:
        print("こんにちは")
        # Display.face_smile()
        OutSound.greet_afternoon()

    elif "こんばんは" in command:
        print("こんばんは")
        # Display.face_smile()
        OutSound.greet_night()

    elif "さようなら" in command:
        print("さようなら")
        # Display.face_smile()
        OutSound.bye()
    
    elif "いってきます" in command:
        print("いってきます")
        # Display.face_smile()
        OutSound.im_going()

    elif "おかえりなさい" in command:
        print("おかえりなさい")
        # Display.face_smile()
        OutSound.welcome_home()

    elif "おやすみ" in command:
    #「目を閉じる」DisplayProcessに遷移
        # Display.face_sleep()
        OutSound.good_night()

#キーワードコマンド

    elif "いいね" in command:
        print("いいね")
        # Display.face_embarrassed()
        OutSound.welcome_home()

    elif "体調が悪い" in command:
        print("体調が悪い")
        # Display.face_sad()
        OutSound.welcome_home()

    elif "体調がいい" in command:
        print("体調がいい")
        # Display.face_smile()
        OutSound.welcome_home()

    elif "誕生日" in command:
        print("誕生日")
        # Display.face_kirarin()
        OutSound.welcome_home()

    elif "ハッピーバースデー" in command:
        print("ハッピーバースデー")
        # Display.face_kirarin()
        OutSound.welcome_home()

    elif "いい気分" in command:
        print("いい気分")
        # Display.face_smile()
        OutSound.welcome_home()

    elif "かっこいい" in command:
        print("かっこいい")
        # Display.face_wink()
        OutSound.welcome_home()

    elif "癒してほしい" in command:
        print("癒してほしい")
        # Display.face_wink()
        OutSound.playMusic()
        # OutSound.welcome_home()

    elif "つらい" in command:
        print("つらい")
        # Display.face_sad()
        OutSound.welcome_home()

    elif "疲れた" in command:
        print("疲れた")
        # Display.face_thinEye()
        OutSound.welcome_home()

    elif "しんどい" in command:
        print("しんどい")
        # Display.face_sad()
        OutSound.welcome_home()

    elif "おめでとう" in command:
        print("おめでとう")
        # Display.face_embarrassed()
        OutSound.welcome_home()

    elif "最高" in command:
        print("最高")
        # Display.face_kirarin()
        OutSound.welcome_home()

    elif "憂鬱" in command:
        print("憂鬱")
        # Display.face_sad()
        OutSound.welcome_home()

#　「感情」　*************************************************************       

    elif "驚いた" in command:
        print("驚いた")
        # Display.face_smile()
        OutSound.surprise()

    elif "悲しい" in command:
        print("悲しい")
        # Display.face_sad()
        OutSound.sad()

    elif "こわい" in command:
        print("こわい")
        # Display.face_sad()
        OutSound.fear()

    elif "うれしい" in command:
        print("うれしい")
        # Display.face_embarrassed()
        OutSound.happy()

#　「利用者からの返事」　*************************************************************  

    # elif "わかりました" in command:
    #     print("わかりました")
    #     # Display.face_embarrassed()
    #     OutSound.ok()

    # elif "わかりません" in command:
    #     print("わかりません")
    #     # Display.face_doubt()
    #     OutSound.no()

#　「機能」　*************************************************************  

    elif "音楽を再生して" in command:
        print("音楽を再生します")
        # LED.led_music()
        OutSound.playMusic()

    elif "シャットダウン" in command:
        print("シャットダウン")
        ComandShutdown = "shutdown"
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

# ********************************〔Empath.pyの呼び出し〕*******************************************
def empath_transfer(audio_file):
    if not audio_file:
        print("音声データがありません。")
        return
    
    # 感情分析
    print("感情を分析しています...")
    Empath.empath(audio_file)
