# 音声入力をもとに処理を行うスレッド
import time
import OutSound
import Empath
import InVoice
import Display
import subprocess
# import gpiozero
# import EarProcess

# 音声アシスタントのループ処理
def assistant():
    print("なにをする？")
    while True:
        command, audio_file = InVoice.listen(mic_timeout=5, phrase_time_limit=5, number=0)
        
        if command is None and audio_file is None:
            print("リセットされました。再度話しかけてください。")
            continue

        # エモボットに関連するキーワード
        emobot_keywords = ["エモボット", "エムボット", "えもぼっと", "EMOBOT", "emobot"]
        # 他のアシスタントのキーワード
        other_assistant_keywords = ["アレクサ", "あれくさ", "ALXA", "alxa", "オッケーグーグル", "おっけーぐーぐる", "OK Google", "ヘイシリー", "へいしり", "Hey Siri", "hey siri"]

        # エモボットのキーワードが含まれている場合

        # 以下追加点
        def assistant_inner():
            if any(word in command for word in emobot_keywords):
                order = InVoice.listen(mic_timeout=5, phrase_time_limit=5, number=1)[0]  # 再度5秒間だけONにしてコマンドを聞き取る
                if order:
                    process(order)
                if command is None and audio_file is None:
                    print("リセットされました。再度話しかけてください。")
                    return assistant_inner()
        # 以上追加点

        # if any(word in command for word in emobot_keywords):
        #     order = InVoice.listen(mic_timeout=5, phrase_time_limit=5)[0]  # 再度5秒間だけONにしてコマンドを聞き取る
        #     if order:
        #         process(order)

        # # 他のアシスタントのキーワードが含まれている場合
        # elif any(word in command for word in other_assistant_keywords):
        #     angry()
        
        # 想定外のキーワードの場合
            else:
                empath_transfer(audio_file)
                print("なんて言ったかわかんないなぁ")

def process(command):
    print("音声入力をもとに処理を行います")

    #　「あいさつ」　*************************************************************   

    if "おはよう" in command:        
        print("おはよう")
        Display.face_smile()
        OutSound.greet_morning()

    elif "こんにちは" in command:
        print("こんにちは")
        Display.face_smile()
        OutSound.greet_afternoon()

    elif "こんばんは" in command:
        print("こんばんは")
        Display.face_smile()
        OutSound.greet_night()

    elif "さようなら" in command:
        print("さようなら")
        Display.face_smile()
        OutSound.bye()
    
    elif "いってきます" in command:
        print("いってきます")
        Display.face_smile()
        OutSound.im_going()

    elif "おかえりなさい" in command:
        print("おかえりなさい")
        Display.face_smile()
        OutSound.welcome_home()

    elif "おやすみ" in command:
    #「目を閉じる」DisplayProcessに遷移
        Display.face_sleep()
        OutSound.good_night()

#キーワードコマンド

    elif "いいね" in command:
        print("いいね")
        Display.face_embarrassed()
        OutSound.welcome_home()

    elif "体調が悪い" in command:
        print("体調が悪い")
        Display.face_sad()
        OutSound.welcome_home()

    elif "体調がいい" in command:
        print("体調がいい")
        Display.face_smile()
        OutSound.welcome_home()

    elif "誕生日" in command:
        print("誕生日")
        Display.face_kirarin()
        OutSound.welcome_home()

    elif "ハッピーバースデー" in command:
        print("ハッピーバースデー")
        Display.face_kirarin()
        OutSound.welcome_home()

    elif "いい気分" in command:
        print("いい気分")
        Display.face_smile()
        OutSound.welcome_home()

    elif "かっこいい" in command:
        print("かっこいい")
        Display.face_wink()
        OutSound.welcome_home()

    elif "癒してほしい" in command:
        print("癒してほしい")
        Display.face_wink()
        OutSound.playMusic()
        # OutSound.welcome_home()

    elif "つらい" in command:
        print("つらい")
        Display.face_sad()
        OutSound.welcome_home()

    elif "疲れた" in command:
        print("疲れた")
        Display.face_thinEye()
        OutSound.welcome_home()

    elif "しんどい" in command:
        print("しんどい")
        Display.face_sad()
        OutSound.welcome_home()

    elif "おめでとう" in command:
        print("おめでとう")
        Display.face_embarrassed()
        OutSound.welcome_home()

    elif "最高" in command:
        print("最高")
        Display.face_kirarin()
        OutSound.welcome_home()

    elif "憂鬱" in command:
        print("憂鬱")
        Display.face_sad()
        OutSound.welcome_home()

#　「感情」　*************************************************************       

    elif "驚いた" in command:
        print("驚いた")
        Display.face_smile()
        OutSound.surprise()

    elif "悲しい" in command:
        print("悲しい")
        Display.face_sad()
        OutSound.sad()

    elif "こわい" in command:
        print("こわい")
        Display.face_sad()
        OutSound.fear()

    elif "うれしい" in command:
        print("うれしい")
        Display.face_embarrassed()
        OutSound.happy()

#　「利用者からの返事」　*************************************************************  

    elif "わかりました" in command:
        print("わかりました")
        Display.face_embarrassed()
        OutSound.ok()

    elif "わかりません" in command:
        print("わかりません")
        Display.face_doubt()
        OutSound.no()

#　「機能」　*************************************************************  

    elif "音楽を再生して" in command:
        print("音楽を再生します")
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
        print("なんて言ったかわかんないなぁ")

# ********************************〔Empath.pyの呼び出し〕*******************************************
def empath_transfer(audio_file):
    if not audio_file:
        print("音声データがありません。")
        return
    
    # 感情分析
    print("感情を分析しています...")
    Empath.empath(audio_file)
