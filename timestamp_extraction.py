import os
import sys
import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim

class tse:
    def __init__(self, images, imagepath='control_images/'):
        self.xmin = [32, 48, 79, 95, 127, 143, 159, 178, 271, 288, 320, 336, 367, 384]
        self.xmax = [47, 63, 94, 110, 142, 158, 174, 193, 286, 303, 335, 351, 382, 399]
        self.xtimemin = [271, 288, 320, 336, 367, 384]
        self.xtimemax = [286, 303, 335, 351, 382, 399]
        self.xdmymin = [32, 48, 79, 95, 127, 143, 159, 178]
        self.xdmymax = [47, 63, 94, 110, 142, 158, 174, 193]
        self.noofcrops = len(self.xmin)
        self.noofcropstime = len(self.xtimemin)
        self.noofcropsdmy = len(self.xdmymin)
        self.images = images
        try:
            self.imagepath = imagepath
            len(os.listdir(self.imagepath))
        except FileNotFoundError:
            print("Control images not found at " + self.imagepath)
            sys.exit()

    def compare_with_control(self, imageA, imageB):
        s = ssim(imageA, imageB, channelaxis=2)
        return s

    def get_datetime_crops(self, img):
        digitcrops = []
        dir_of_control = os.listdir(self.imagepath)
        amt_control_imgs = len(dir_of_control)
        for i in range(self.noofcrops):
            crops = img[64:84, self.xmin[i]:self.xmax[i]]
            crops = cv2.cvtColor(crops, cv2.COLOR_BGR2GRAY)
            average_color = np.average(np.average(crops, axis=0), axis=0)
            if average_color > 100:
                _, thres = cv2.threshold(crops, 200, 255, cv2.THRESH_BINARY)
            else:
                _, thres = cv2.threshold(crops, 50, 255, cv2.THRESH_BINARY_INV)
            similarity = []
            for j in range(0, amt_control_imgs):
                img2 = cv2.imread(self.imagepath + dir_of_control[j])
                img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
                similarity.append(self.compare_with_control(thres, img2))
            digitcrops.append(dir_of_control[similarity.index(max(similarity))].split('_')[0])
        return digitcrops

    def get_time_crops(self, img):
        digitcrops = []
        dir_of_control = os.listdir(self.imagepath)
        amt_control_imgs = len(dir_of_control)
        for i in range(self.noofcropstime):
            crops = img[64:84, self.xtimemin[i]:self.xtimemax[i]]
            crops = cv2.cvtColor(crops, cv2.COLOR_BGR2GRAY)
            average_color = np.average(np.average(crops, axis=0), axis=0)
            if average_color > 100:
                _, thres = cv2.threshold(crops, 200, 255, cv2.THRESH_BINARY)
            else:
                _, thres = cv2.threshold(crops, 50, 255, cv2.THRESH_BINARY_INV)
            similarity = []
            for j in range(0, amt_control_imgs):
                img2 = cv2.imread(self.imagepath + dir_of_control[j])
                img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
                similarity.append(self.compare_with_control(thres, img2))
            digitcrops.append(dir_of_control[similarity.index(max(similarity))].split('_')[0])
        return digitcrops

    def get_dmy_crops(self, img):
        digitcrops = []
        dir_of_control = os.listdir(self.imagepath)
        amt_control_imgs = len(dir_of_control)
        for i in range(self.noofcropsdmy):
            crops = img[64:84, self.xdmymin[i]:self.xdmymax[i]]
            crops = cv2.cvtColor(crops, cv2.COLOR_BGR2GRAY)
            average_color = np.average(np.average(crops, axis=0), axis=0)
            if average_color > 100:
                _, thres = cv2.threshold(crops, 200, 255, cv2.THRESH_BINARY)
            else:
                _, thres = cv2.threshold(crops, 50, 255, cv2.THRESH_BINARY_INV)
            similarity = []
            for j in range(0, amt_control_imgs):
                img2 = cv2.imread(self.imagepath + dir_of_control[j])
                img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
                similarity.append(self.compare_with_control(thres, img2))
            digitcrops.append(dir_of_control[similarity.index(max(similarity))].split('_')[0])
        return digitcrops

    def extraction_datetime(self):
        digitcrops = self.get_datetime_crops(self.images)
        print(digitcrops)
        date = str(digitcrops[0]) + str(digitcrops[1])
        month = str(digitcrops[2]) + str(digitcrops[3])
        year = str(digitcrops[4]) + str(digitcrops[5]) + str(digitcrops[6]) + str(digitcrops[7])
        hour = str(digitcrops[8]) + str(digitcrops[9])
        minute = str(digitcrops[10]) + str(digitcrops[11])
        second = str(digitcrops[12]) + str(digitcrops[13])
        return date, month, year, hour, minute, second

    def extraction_dmy(self):
        digitcrops = self.get_dmy_crops(self.images)
        print(digitcrops)
        date = str(digitcrops[0]) + str(digitcrops[1])
        month = str(digitcrops[2]) + str(digitcrops[3])
        year = str(digitcrops[4]) + str(digitcrops[5]) + str(digitcrops[6]) + str(digitcrops[7])
        return date, month, year

    def extraction_time(self):
        digitcrops = self.get_time_crops(self.images)
        print(digitcrops)
        hour = str(digitcrops[0]) + str(digitcrops[1])
        minute = str(digitcrops[2]) + str(digitcrops[3])
        second = str(digitcrops[4]) + str(digitcrops[5])
        return hour, minute, second
