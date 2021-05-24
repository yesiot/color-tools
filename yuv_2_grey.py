import os
import sys

from PIL import Image

input_name = sys.argv[1]
output_name = sys.argv[2]
img_width = int(sys.argv[3])
img_height = int(sys.argv[4])

with open(input_name, "rb") as src_file:
    raw_data = src_file.read()
    img = Image.frombuffer("L", (img_width, img_height), raw_data[0::2])
    img.show()
