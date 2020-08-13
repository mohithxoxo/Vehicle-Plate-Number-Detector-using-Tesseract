import pytesseract
pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
print('Tesseract-OCR Loaded')
import cv2
import imutils
import numpy as np

while True:
    print('Enter Vehicle Image Path')
    path = input()
    image = cv2.imread(path)
    image = imutils.resize(image , width = 500)
    gray = cv2.cvtColor(image , cv2.COLOR_BGRA2GRAY)
    gray = cv2.bilateralFilter(gray , 11 , 17 ,17)
    edged = cv2.Canny(gray , 170 , 200)
    cnts , new = cv2.findContours(edged.copy() , cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    image1 = image.copy()
    cv2.drawContours(image1 , cnts , -1 ,(0,255,0),3)
    cnts = sorted(cnts , key = cv2.contourArea , reverse = True)[:30]
    NumberPlateCount= None
    image2 = image.copy()
    cv2.drawContours(image2 , cnts , -1 ,(0,255,0),3)
    count = 0
    name = 1
    for i in cnts:
        prm = cv2.arcLength(i, True)
        approx = cv2.approxPolyDP(i, 0.02*prm , True)
        if(len(approx) == 4):
            NumberPlateCount = approx
            x , y , w , h = cv2.boundingRect(i)
            crp_img = image[y:y+h , x:x+w]
            cv2.imwrite(str(name)+'.png',crp_img)
            name == 1
            break
        
    cv2.drawContours(image,[NumberPlateCount], -1 ,(0,255,0),3)
    crop_img_loc = '1.png'
    cv2.imshow("Cropped Image ", cv2.imread(crop_img_loc))

    text = pytesseract.image_to_string(crop_img_loc)
    print('Plate Number is :',text)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
