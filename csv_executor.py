import csv
import os
from PIL import Image, ImageDraw


class Mnemo_Image:
    def  __init__(self, path_to_csv_config, result_folder, source_folder):
        self.path_to_csv_config = path_to_csv_config
        self.result_folder = result_folder
        self.source_folder = source_folder
        with open(path_to_csv_config, 'r') as csv_file:
            self.reader = csv.reader(csv_file)
            next(self.reader)
            self.data = list(self.reader)
    
    def process_input(self):
        input_dirs = os.listdir(self.source_folder)
        for row in self.data:
            if row[0] in input_dirs:
                create_folder(self.result_folder + '/' + row[0]+ '/' + row[1])
            source_imgs_names = os.listdir(self.source_folder + '/' + row[0])
            print(source_imgs_names)
            for source_img in source_imgs_names:
                crop_img(self.source_folder + '/' + row[0] +'/'+ source_img, row[2], row[3], row[4], row[5]).save(self.result_folder + '/' + row[0]+ '/' + row[1] + '/' + source_img)


def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)

def crop_img(img_path, x1, y1, x2, y2):
    img = Image.open(img_path)
    x1, y1, x2, y2 = map(int, (x1, y1, x2, y2))
    cropped_img = img.crop((x1, y1, x2, y2))
    return cropped_img

if __name__ == "__main__":
    mi = Mnemo_Image('rec_definer.csv', 'result_folder', 'source_photo')
    mi.process_input()