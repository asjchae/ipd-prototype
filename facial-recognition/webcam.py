import cv
import cv2
import time
from PIL import Image
import numpy as np
import csv


if __name__ == '__main__':

    """
    open webcam and capture images
    """
    cv2.namedWindow("Webcam")
    vc = cv2.VideoCapture(0)

    if vc.isOpened(): # try to get the first frame
        rval, frame = vc.read()
    else:
        rval = False

    print "\n\n\n\n\npress space to take picture; press ESC to exit"

    while rval:
        cv2.imshow("Webcam", frame)
        rval, frame = vc.read()
        key = cv2.waitKey(40)
        if key == 27: # exit on ESC
            break
        if key == 32: # press space to save images
            cv.SaveImage("webcam.jpg", cv.fromarray(frame))
            img = cv.LoadImage("webcam.jpg") # input image
    
    cv2.destroyWindow("preview")
