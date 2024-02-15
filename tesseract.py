import pytesseract
import cv2
import numpy as np
from PIL import Image

if __name__ == "__main__":
    # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    img = cv2.imread('result_folder/m_e/air_clr_c_f_w_out_temp_1/1.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    digit_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > 100]
    for cnt in digit_contours:
        x, y, w, h = cv2.boundingRect(cnt)
        digit_roi = thresh[y:y+h, x:x+w]
        custom_config = r'--oem 3 --psm 6 outputbase digits'
        digit_text = pytesseract.image_to_string(Image.fromarray(digit_roi), config=custom_config)
        print("Digit Text:", digit_text)
    # cv2.imshow("Thresh", thresh)
    cv2.waitKey(0)
    cv2.destroyAllWindows()