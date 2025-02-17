-import cv2

# Haar Cascade の分類器をロード
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# カメラ映像をキャプチャする
cap = cv2.VideoCapture(0)

# フレームレート、解像度を設定する
cap.set(cv2.CAP_PROP_FPS, 120)  # 30 FPS
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)  # 幅 1280
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)  # 高さ 720

while True:
    # フレームをキャプチャする
    ret, frame = cap.read()

    # フレームの取得に成功しているか確認
    if not ret:
        print("フレームの取得に失敗しました。")
        break
    
    # 画像をグレースケールに変換
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # 顔を検出
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=12, minSize=(10, 10))
    
    # 検出した顔に四角形を描く
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    # フレームを表示する
    cv2.imshow('Face Detection', frame)
    
    # 'q' キーが押されたらループを終了
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    cv2.putText(frame, "text", (100,100), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 5, (0, 0, 255), 2, cv2.LINE_AA	, bottomLeftOrigin=False)



# キャプチャとウィンドウを解放
cap.release()
cv2.destroyAllWindows()
