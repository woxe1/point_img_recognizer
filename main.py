from PIL import Image, ImageDraw


if __name__ == "__main__":
    image_path = 'source_photo/m_e/3_me.jpg'
    img = Image.open(image_path)
    cropped_img = img.crop((4450, 1190, 4610, 1281))
    cropped_img.save('./ph.jpg')
    cropped_img.show()


