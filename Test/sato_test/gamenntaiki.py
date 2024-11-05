import cv2

def standbydisplay (displayflag):
    displayflag = "stand"
    image_path = 'YuuTaTaNaKa/EMOBOT/Test/sato_test/tozime.png'
    
    # 画像を読み込む
    image = cv2.imread(image_path)
    
    if image is not None:
        # 画像を表示する
        cv2.imshow('Displayed Image', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print(f"Error: Could not open or find the image at path {image_path}")
