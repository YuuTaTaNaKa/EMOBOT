import cv2
import matplotlib.pyplot as plt

img = cv2.imread('Test\CV2\img\kirei.jpg')
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)) 

plt.show()