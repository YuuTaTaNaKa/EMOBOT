import cv2

def executiondisplay(displayflag):
    # 画像と表示秒数のリストを定義
    images_and_times = [
        (cv2.imread('YuuTaTaNaKa/EMOBOT/Test/sato_test/me100.png'), 8),  # 3秒表示
        (cv2.imread('YuuTaTaNaKa/EMOBOT/Test/sato_test/me50.png'), 1),   # 2秒表示
        (cv2.imread('YuuTaTaNaKa/EMOBOT/Test/sato_test/tozime.png'), 1)   # 1秒表示
    ]
    
    for image, display_time in images_and_times:
        if image is not None:
            cv2.imshow('Display', image)  # 画像を表示
            cv2.waitKey(display_time * 1000)  # 各画像ごとの秒数をミリ秒で指定
        else:
            print("画像が読み込めませんでした。パスを確認してください。")
    
    # すべての画像表示が終わったらウィンドウを閉じる
    cv2.destroyAllWindows()

# 関数を呼び出して実行
executiondisplay(displayflag=True)
