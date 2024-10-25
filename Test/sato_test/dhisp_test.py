import cv2

image = cv2.imread('fubuki.jpg')
cv2.imshow('Displayed Image', image)
cv2.waitKey(0) 
cv2.destroyAllWindows()