import os
import sys
import cv2
import numpy as np

input_name = sys.argv[1]
output_name = sys.argv[2]
img_width = int(sys.argv[3])
img_height = int(sys.argv[4])


with open(input_name, "rb") as src_file:
    raw_data = np.fromfile(src_file, dtype=np.uint8, count=img_width*img_height*2)
    im = raw_data.reshape(img_height, img_width, 2)

    rgb = cv2.cvtColor(im, cv2.COLOR_YUV2BGR_YUYV)
    
    if output_name != 'cv':
        cv2.imwrite(output_name, rgb)
    else:
        cv2.imshow('', rgb)
        cv2.waitKey(0)


