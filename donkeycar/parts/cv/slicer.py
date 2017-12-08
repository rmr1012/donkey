import cv2
import numpy as np

class slicer():
    
    def __init__(self):
        print("I'm tiny rick!!")
    def run(self, img_arr):
        print("bro lol")
        img_arr_t,img_arr_b,crap = cv2.split(img_arr)
        return img_arr_t,img_arr_b


    def update(self):
        pass
