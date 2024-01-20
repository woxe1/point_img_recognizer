import easyocr

if __name__ == "__main__":
    reader = easyocr.Reader(['en'])
    result = reader.readtext('result_folder/m_e/start_air/1.jpg')
    for detection in result:
        print(detection[1])