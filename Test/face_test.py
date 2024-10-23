import cv2

# カメラ映像をキャプチャする
video_capture = cv2.VideoCapture(0)

while True:
    # ビデオフレームを取得
    ret, frame = video_capture.read()

    # ビデオフレームを表示
    cv2.imshow('EMOBOT', frame)

    # 'q' キーが押されたらループを終了
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# カメラとウィンドウを解放
video_capture.release()
cv2.destroyAllWindows()

"""
必要なライブラリのインストールコマンド（ターミナルで行う）
pip install opencv-python
pip install dlib
pip install face_recognition
"""