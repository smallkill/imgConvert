#!/usr/bin/python
#-*- coding: UTF-8 -*-

import numpy as np
import os
import math
import cv2
import sys
import glob
import time

# Fillter images file
def is_imag(filename):
    return os.path.splitext(filename)[-1] in [".png", ".jpg", ".bmp"]

def convertImg(path):
    img = cv2.imread(path,1)
    cv2.imshow("img",img)
    cv2.waitKey(1)
    return img

def main():

    # get all parameter
    """
        imgConvert.py dirIn dirOut extFormat numofdig startindex
    """

    dirnameIn = sys.argv[1]
    dirnameOut = sys.argv[2]
    extformat = sys.argv[3]
    numofdig = sys.argv[4]
    startindex = sys.argv[5]
    
    print ("import direct name:" + dirnameIn)
    print ("export direct name:" + dirnameOut)
    print ("ext file format:" + extformat)
    print ("number of digits:" + numofdig)
    print ("start index:" + startindex)

    # Get direction path
    filenames = os.listdir(dirnameIn)
    
    # Get file name and filter the images
    images = list(filter(is_imag, filenames))
    
    numofImg = len(images)
    print ( "total images:" + str(numofImg))

    count = 0

    for img in images:

        # get real image
        pathIn = os.path.join(dirnameIn,img) 
        outimg = convertImg(pathIn)
        
        # saving images
        fileNo = str(count).zfill(int(numofdig))
        pathOut = dirnameOut + fileNo + "." + extformat
        cv2.imwrite(pathOut,outimg)

        count = count + 1
        print ( "\rprogress : %.2f " % round(count/numofImg*100,2) + "% " , end="")

    print ("\n===== complete !!! =====")

if __name__ == "__main__":
    main()

