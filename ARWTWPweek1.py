"""This script should iterate through a list of images, rotate, resize and convert them"""

import os
from PIL import Image
from contextlib import chdir
os.chdir(r"C:\Users\Usuario\Documents\ARWTWP\week1\images")
for item in os.listdir()[1:]:
    with Image.open(item) as im:
        if im.mode != 'RGB':
            im = im.convert('RGB')
        im.rotate(270).resize((128,128)).save(item + ".jpeg")