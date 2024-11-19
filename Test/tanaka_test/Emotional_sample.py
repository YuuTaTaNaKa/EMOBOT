# from feat import Detector
# from feat.utils.io import get_test_data_path
# import matplotlib.pyplot as plt
# import os
# from scipy.integrate import simps

# # 検出器の定義
# detector = Detector()

# # 公式が用意した画像のパスを取得
# test_data_dir = get_test_data_path()
# single_face_img_path = os.path.join(test_data_dir, "single_face.jpg")

# # 画像を指定して表情認識を実行
# detector.detect_image('<smailes-bring-happiness.jpeg>')
# result = detector.detect_image(single_face_img_path)

# # 結果を出力
# result.plot_detections()
# plt.show()



from feat import Detector
import numpy as np
import cv2
from scipy.integrate import simps

detector = Detector(
    face_model="retinaface",
    landmark_model="mobilefacenet",
    au_model='jaanet', # ['svm', 'logistic', 'jaanet']
    emotion_model="resmasknet",
)

single_face_prediction = detector.detect_image("smailes-bring-happiness.jpeg")
# single_face_prediction = detector.detect_image("smailes-bring-happiness.jpeg", outputFname = "output.csv")

print(single_face_prediction.facebox)
print(single_face_prediction.aus)
print(single_face_prediction.emotions)
print(single_face_prediction.facepose) # (in degrees)
# figs = single_face_prediction.plot_detections(poses=True)
figs = single_face_prediction.plot_detections(faces='aus', muscles=True)
print(len(figs)) # 1

figs[0].canvas.draw()
image = np.array(figs[0].canvas.renderer.buffer_rgba())
# image = np.array(figs[0].canvas.renderer._renderer)
image = cv2.cvtColor(image, cv2.COLOR_RGBA2BGR)

cv2.imshow("image", image)
cv2.waitKey(0)
