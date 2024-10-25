import cv2
from light_senti_analysis.py import emotion

if (emotion == "positive"):
    image = cv2.imread('Test/sato_test/fubuki.jpg')
    cv2.imshow('Displayed Image', image)
    cv2.waitKey(0) 
    cv2.destroyAllWindows()
elif(emotion == "positive"):
    image = cv2.imread('Test/sato_test/fubuki.jpg')
    cv2.imshow('Displayed Image', image)
    cv2.waitKey(0) 
    cv2.destroyAllWindows()
else:
    image = cv2.imread('Test/sato_test/fubuki.jpg')
    cv2.imshow('Displayed Image', image)
    cv2.waitKey(0) 
    cv2.destroyAllWindows()
