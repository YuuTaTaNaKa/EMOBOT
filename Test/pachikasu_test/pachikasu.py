import cv2

image_file = 'cat.png'
img = cv2.imread(image_file)
cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()