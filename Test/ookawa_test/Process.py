# 音声入力をもとに処理を行うスレッド
import time
import OutSound
import Empath
import InVoice
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
        def assistant_1():
            if any(word in command for word in emobot_keywords):
                order = InVoice.listen(mic_timeout=5, phrase_time_limit=5, number=1)[0]  # 再度5秒間だけONにしてコマンドを聞き取る
                if order:
                    process(order)
                if command is None and audio_file is None:
                    print("リセットされました。再度話しかけてください。")
                    return assistant_1()
        # 以上追加点
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
        OutSound.greet_morning()

    elif "こんにちは" in command:
        print("こんにちは")
        OutSound.greet_afternoon()

    elif "こんばんは" in command:
        print("こんばんは")
        OutSound.greet_night()

    elif "さようなら" in command:
        print("さようなら")
        OutSound.bye()
    
    elif "いってきます" in command:
        print("いってきます")
        OutSound.im_going()

    elif "おかえりなさい" in command:
        print("おかえりなさい")
        OutSound.welcome_home()

    elif "おやすみ" in command:
    #「目を閉じる」DisplayProcessに遷移
        Display.close_eyes()
        OutSound.good_night()

#キーワードコマンド

    elif "いいね" in command:
        print("いいね")
        OutSound.welcome_home()

    elif "体調が悪い" in command:
        print("体調が悪い")
        OutSound.welcome_home()

    elif "体調がいい" in command:
        print("体調がいい")
        OutSound.welcome_home()

    elif "体調がいい" in command:
        print("体調がいい")
        OutSound.welcome_home()

    elif "誕生日" in command:
        print("誕生日")
        OutSound.welcome_home()

    elif "ハッピーバースデー" in command:
        print("ハッピーバースデー")
        OutSound.welcome_home()

    elif "いい気分" in command:
        print("いい気分")
        OutSound.welcome_home()

    elif "かっこいい" in command:
            print("かっこいい")
            OutSound.welcome_home()

    elif "癒してほしい" in command:
        print("癒してほしい")
        OutSound.welcome_home()

    elif "つらい" in command:
        print("つらい")
        OutSound.welcome_home()

    elif "疲れた" in command:
            print("疲れた")
            OutSound.welcome_home()

    elif "しんどい" in command:
            print("しんどい")
            OutSound.welcome_home()

    elif "おめでとう" in command:
            print("おめでとう")
            OutSound.welcome_home()

    elif "最高" in command:
            print("最高")
            OutSound.welcome_home()

    elif "憂鬱" in command:
            print("憂鬱")
            OutSound.welcome_home()

#　「感情」　*************************************************************       

    elif "驚き" in command:
        print("驚き")
        OutSound.surprise()

    elif "悲しい" in command:
        print("悲しい")
        OutSound.sad()

    elif "恐れ" in command:
        print("恐れ")
        OutSound.fear()

    elif "うれしい" in command:
        print("うれしい")
        OutSound.happy()

#　「利用者からの返事」　*************************************************************  

    elif "わかりました" in command:
        print("わかりました")
        OutSound.ok()

    elif "わかりません" in command:
        print("わかりません")
        OutSound.no()

#　「機能」　*************************************************************  

    elif "音楽を再生して" in command:
        print("音楽を再生します")
        OutSound.playMusic()

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
