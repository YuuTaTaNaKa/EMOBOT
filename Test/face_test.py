import cv2

# カメラ映像をキャプチャする
video_capture = cv2.VideoCapture(0)

while True:
    # ビデオフレームを取得
    ret, frame = video_capture.read()

    # ビデオフレームを表示
    cv2.imshow('Video', frame)

    # 'q' キーが押されたらループを終了
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# カメラとウィンドウを解放
video_capture.release()
cv2.destroyAllWindows()

"""
必要なライブラリのインストールコマンド（ターミナルで行う）
pip install opencv-python
pip install dlib
pip install face_recognition
"""