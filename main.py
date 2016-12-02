from __future__ import division
import math
import cv2
import numpy as np
import os
import time
import csv
import sys

class Slide:
    def __init__(self,filename):
        self.bgr = cv2.imread(filename)
        self.gray = cv2.imread(filename, 0)
    def mask(self, hl,hh,sl,sh,vl,vh): # hsv theshold parameters
        hsv = cv2.cvtColor(self.bgr, cv2.COLOR_BGR2HSV)
        lower_bound = np.array([hl,sl,vl],dtype=np.uint8)
        upper_bound = np.array([hh,sh,vh],dtype=np.uint8)
        return cv2.inRange(hsv, lower_bound,upper_bound)
    def apPixelRaw(self):
        return cv2.countNonZero(self.mask(150,185, 40,220, 65,240))
    def dabPixelRaw(self):
        return cv2.countNonZero(self.mask(3,20, 60,180, 25,250))
    def dab(self):
        maskdab = self.mask(3,20, 60,180, 25,250)
        return cv2.bitwise_and(self.bgr, self.bgr, mask = maskdab)
    def ap(self):
        maskap = self.mask(150,185, 40,220, 65,240)
        return cv2.bitwise_and(self.bgr, self.bgr, mask = maskap)
    def background(self): #fix erosion bounds
        kernel = np.ones((4,4),np.uint8)
        eroded =  cv2.erode(self.gray,kernel,iterations=2)
        ret,thresh = cv2.threshold(eroded, 200,255,cv2.THRESH_BINARY_INV)
        return cv2.bitwise_and(self.bgr, self.bgr, mask = thresh)

class Contour:
    def __init__(self, layer):
        self.layer = layer
        self.bgr= cv2.imread(filename)
    def contourData(self, dilate = 2): # contract into class as init
        gray = cv2.cvtColor(self.layer, cv2.COLOR_BGR2GRAY)
        kernel = np.ones((dilate,dilate),np.uint8)
        dilatedGray = cv2.dilate(gray,kernel,iterations=2)
        ret, thresh = cv2.threshold(dilatedGray, 1,255,cv2.THRESH_BINARY)
        image, contoursData, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
        drawn = cv2.drawContours(image,contoursData,-1,(150,150,150),3)
        return contoursData, drawn
    def geoCenters(self):
        contours = self.contourData()[0]
        coordinates = []
        for contour in contours:
            moments = cv2.moments(contour)
            contourX = int(moments['m10'] / float(moments['m00']))
            contourY = int(moments['m01'] / float(moments['m00']))
            coordinates += [[contourX, contourY]]
        return coordinates
    def areaNoise(self, minArea):
        contours = self.contourData()[0]
        lessThanMin = []
        for contour in contours:
            if cv2.contourArea(contour) <= minArea:
                lessThanMin.append(contour)
        return sum(lessThanMin)
    def radii(self):
        contours = self.contourData()[0]
        radii = []
        for contour in contours:
            radius = math.sqrt(cv2.contourArea(contour)/math.pi)
            radii.append(radius)
        return radii
    def distanceInClass(geoCenters, radii):
        distances = []
        while (len(geoCenters) > 1):
            i = len(geoGenters)
            x1, y1 = geoCenters.pop() # set x,y to the last element, discard
            for x2,y2 in geoCenters:
                hypot = math.sqrt((x2-x1)**2+(y2-y1)**2) #compute distance
                distances.append(hypot-radii[i])
        return distances

def colocalization(contoursA, contoursB, minDist): #proportion of distances between sets under some constant distance, assuming granular contour shape
    rawDistances = []
    for x1,y1 in contoursA.geoCenters():
        for x2, y2 in contoursB.geocenters():
            rawDistances.append(math.sqrt((x2-x1)**2+(y2-y1)**2))
        areaCorrection = []
    for radiusA in contoursA.radii():
        for radiusB in contoursB.radii():
            correction = radiusA + radiusB
            areaCorrection.append(correction)
    correctedDistances = []
    for i in len(rawDistances):
        correctedDistance = rawDistance[i]-areaCorrection[i]
        correctedDistances.append(correctedDistance)
    underMin = 0
    for correctedDistance in correctedDistances:
        if correctedDistance < minDist:
            underMin = underMin + 1
    return underMin/len(correctedDistance)

if __name__ == "__main__":
    path = "./" + argv[1]
    files = [str(filename) for filename in os.listdir(path)]
    count = []
    for filename in os.listdir(path):
        if filename.endswith("png"):
            a = Slide("./images/" + filename)
            a.dab()
            b = Contour(a.dab(),filename)
            print("cells counted for file " + filename + " = " + str(b.cellCount()))
