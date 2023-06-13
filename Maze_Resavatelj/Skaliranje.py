import cv2
import numpy as np
from Point import Pt
import math

def skaliraj(image):
    gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gray,(5,5), cv2.BORDER_DEFAULT)
    ret, thresh = cv2.threshold(blur, 100, 255, cv2.THRESH_BINARY_INV)
    return gray
