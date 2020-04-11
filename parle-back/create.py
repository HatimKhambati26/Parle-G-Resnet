# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 00:15:56 2020

@author: KumKap
"""

import cv2 as cv
import numpy as np
import xml.etree.ElementTree as ET
import os


main_file = 'C:\\Users\KumKap\\opencv\\annots'

for r, d, f in os.walk(main_file):
    print(f)
    for file in f:
        tree = ET.parse(main_file + "\\" + file)
        root = tree.getroot()
        imgfile = root[1].text
        xmin = int(root[6][4][0].text)
        ymin = int(root[6][4][1].text)
        xmax = int(root[6][4][2].text)
        ymax = int(root[6][4][3].text)
        imgfile = imgfile[1:]
        
        path = main_file + "\\" + imgfile
        imagine = cv.imread('C:\\Users\\KumKap\\opencv\\images\\' + imgfile,1)
        #print(xmin+xmax+ymin+ymax)
        crop_img = imagine[ymin:ymax, xmin:xmax]
        cv.imwrite(imgfile, crop_img)
        #cv.imwrite(path, crop_img, [int(cv.IMWRITE_JPEG_QUALITY), 100])
