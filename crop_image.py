import os
import PIL as pl
from PIL import Image

BASE_DIR = os.getcwd()
TO_BE_CROPPED_DIR = os.path.join(BASE_DIR, 'to_be_cropped')
CROPPED_DIR = os.path.join(BASE_DIR, 'cropped')
all_files_to_be_cropped = os.listdir(TO_BE_CROPPED_DIR)
filepath_ref = os.path.join(BASE_DIR, 'reference.jpg')
with pl.Image.open(filepath_ref) as img:
    width_ref, height_ref = img.size

for file in all_files_to_be_cropped:
    filepath=os.path.join(TO_BE_CROPPED_DIR, file)
    with Image.open(filepath) as img:
        width, height = img.size
        x_coord_left  = (width-width_ref)/2
        x_coord_right = (width-width_ref)/2 + width_ref
        y_coord_up = (height-height_ref)/2
        y_coord_bottom = (height-height_ref)/2 + height_ref
        cropped_image = img.crop((x_coord_left, y_coord_up, x_coord_right, y_coord_bottom))
        cropped_image.save(os.path.join(CROPPED_DIR, file))

