# simple script to help convert between image formats to PNG format non-destructively

from PIL import Image
import sys
import os

# python format.py [path to images] [original extention]

if __name__ == "__main__":
    img_dir = str(sys.argv[1])
    ext_i = str(sys.argv[2])
    for f in os.listdir(img_dir):
        if f.endswith(ext_i):
            file_path = img_dir + "/" + f
            img = Image.open(file_path)
            len_ext_i = len(ext_i) + 1 if ext_i.startswith(".") else len(ext_i) # strip "."
            file_out = f[:-len_ext_i] + "png"
            img.save(img_dir + "/" + file_out)
    print("files saved in " + img_dir)
