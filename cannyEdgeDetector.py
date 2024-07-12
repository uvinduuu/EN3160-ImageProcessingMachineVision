# Meaning of low-threshold and high-threshold
import cv2 as cv
import numpy as np
import math
hi_threshold_max = 255
title_window = r'Canny'

ratio = 0.3 # Low threshold/Hi threshold
hi_threshold = 255
low_threshold = math.floor(hi_threshold*ratio)

def on_trackbar(val):
    hi_threshold = cv.getTrackbarPos(trackbar1_name, title_window)
    ratio = cv.getTrackbarPos(trackbar2_name, title_window)/100.
    low_threshold = hi_threshold*ratio
    edges = cv.Canny(im,low_threshold,hi_threshold)
    cv.imshow(title_window, edges)

im = cv.imread('Images-20240703/girl.jpg', cv.IMREAD_COLOR)
if im is None:
    print('Could not open or find the image: ')
    exit(0)

cv.namedWindow(title_window)
trackbar1_name = r'High Threshold Value'
cv.createTrackbar(trackbar1_name, title_window , hi_threshold, hi_threshold_max, on_trackbar)
trackbar2_name = r'Low Threshold %'
cv.createTrackbar(trackbar2_name, title_window , 1, 100, on_trackbar)
on_trackbar(hi_threshold)
cv.waitKey()
cv.destroyAllWindows()