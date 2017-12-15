import cv2
import numpy as np

class slicer():
    
    def __init__(self):
        print("slicer inited")
    def run(self, img_arr):
        #print("slicing..")

        start_row, start_col = int(0), int(0)
        # Let's get the ending pixel coordinates (bottom right of cropped top)
        end_row, end_col = int(height * .5), int(width)
        img_arr_t= img_arr[start_row:end_row , start_col:end_col]

        # Let's get the starting pixel coordiantes (top left of cropped bottom)
        start_row, start_col = int(height * .5), int(0)
        # Let's get the ending pixel coordinates (bottom right of cropped bottom)
        end_row, end_col = int(height), int(width)
        img_arr_b = img_arr[start_row:end_row , start_col:end_col]

        return img_arr_t,img_arr_b


    def update(self):
        pass
