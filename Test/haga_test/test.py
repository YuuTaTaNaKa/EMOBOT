import time
import tkinter as tk

def display():
    print("画面を表示します。")

def on_touch(event):
    print("画面がタッチされました！")

#メインウィンドウの作成
root = tk.Tk()
def on_close():
    print("ウィンドウの閉じるボタンは無効化されています！")

#ウィンドウの閉じるボタンを無効化
root.protocol("WM_DELETE_WINDOW", on_close)

#タイトル
root.title("タッチイベントの例")

#ウィンドウ全体にキャンバスを配置
canvas = tk.Canvas(root, width=800, height=600)  # 液晶の解像度に合わせてサイズを調整
canvas.pack(fill=tk.BOTH, expand=True)

#キャンバスにタッチイベントを結合
canvas.bind("<Button-1>", on_touch)  # 左クリックをタッチイベントとして扱う

def stop():
    print("スレッドを終了します。")
    return

#メインループの開始
root.mainloop()


