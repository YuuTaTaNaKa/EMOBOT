import cv2
import face_recognition

# カメラ映像をキャプチャする
video_capture = cv2.VideoCapture(0)

while True:
    # ビデオフレームを取得
    ret, frame = video_capture.read()

    # 顔認識を行い、顔の位置を取得
    face_locations = face_recognition.face_locations(frame)

    # 検出された顔の周りに枠線を描く
    for (top, right, bottom, left) in face_locations:
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

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