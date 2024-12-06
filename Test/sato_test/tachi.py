import tkinter as tk

def on_touch(event):
    # タッチ座標を取得して表示
    label.config(text=f"Touched at: x={event.x}, y={event.y}")
    print(f"Touched at: x={event.x}, y={event.y}")

def reset_label(event):
    # ラベルをリセット
    label.config(text="Touch the screen to test.")

# メインウィンドウを作成
root = tk.Tk()
root.title("Touch Test")

# ウィンドウサイズを画面全体に拡大
root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
root.attributes("-fullscreen", True)

# タッチイベントを表示するラベル
label = tk.Label(root, text="Touch the screen to test.", font=("Arial", 24))
label.pack(expand=True)

# タッチイベントにバインド
root.bind("<Button-1>", on_touch)  # シングルタッチ（左クリックに相当）
root.bind("<Double-Button-1>", reset_label)  # ダブルタップでリセット

# アプリを起動
root.mainloop()
