import tkinter as tk

# ウィンドウを作成
root = tk.Tk()
root.title("タッチ判定の例")
root.geometry("400x400")

# タッチイベントが発生したかを判定する関数
def on_touch(event):
    label.config(text="タッチされた！")
    # 1秒後にラベルを元に戻す
    root.after(1000, lambda: label.config(text="画面をタッチしてください"))

# キャンバスを作成し、タッチイベントをバインド
canvas = tk.Canvas(root, bg="lightblue", width=400, height=400)
canvas.pack()

# タッチ（クリック）イベントをバインド
canvas.bind("<Button-1>", on_touch)

# 初期メッセージのラベル
label = tk.Label(root, text="画面をタッチしてください", font=("Helvetica", 16))
label.pack(pady=20)

# メインループ
root.mainloop()
