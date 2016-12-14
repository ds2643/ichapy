# image processing functionality modularized

from __future__ import division
import math
import cv2
import numpy as np

class Slide:
    ''' data pipeline created from raw image data; provides mechanism for extracting primitive features of image (e.g., spatially intact representation of those pixels falling within some specified color threshold) '''

    def __init__(self, filename):
        ''' internal representations of image as numpy.ndarray matrix stored to avoid recomputation '''
        self.bgr = cv2.imread(filename)
        self.gray = cv2.imread(filename, 0)
        self.DAB_MASK_VALUES = {
            '''
            NOTE: these hsv values chosen through trial and error
            hl -> hue lower bound
            hh -> hue higher bound
            sl -> saturation lower bound
            sh -> saturation higher bound
            vl -> volume lower bound
            vh -> volume higher bound
            '''
            "hl": 3,
            "hh": 20,
            "sl": 60,
            "sh": 180,
            "vl": 25,
            "vh": 250}
        self.AP_MASK_VALUES = {
            '''
            NOTE: these hsv values chosen through trial and error
            hl -> hue lower bound
            hh -> hue higher bound
            sl -> saturation lower bound
            sh -> saturation higher bound
            vl -> volume lower bound
            vh -> volume higher bound
            '''
            "hl": 150,
            "hh": 185,
            "sl": 40,
            "sh": 220,
            "vl": 65,
            "vh": 240}

    def generate_mask(self, mask): # hsv theshold parameters
        ''' returns a representation of the image thresholded for some specified hsv color range indicated by mask argument '''
        hsv = cv2.cvtColor(self.bgr, cv2.COLOR_BGR2HSV)
        hsv_lower_values = [mask["hl"], mask["sl"], mask["vl"]]
        lower_bound = np.array(hsv_lower_values, dtype=np.uint8)
        hsv_upper_values = [mask["hh"], mask["sh"], mask["vh"]]
        upper_bound = np.array(hsv_upper_values, dtype=np.uint8)
        return cv2.inRange(hsv, lower_bound, upper_bound)

    def custom_pigment(self, mask):
        ''' returns matrix representation of image including only those pixels that fall in the color range specified by the mask HSV threshold specification '''
        assert(isinstance(mask, dict))
        # TODO: assert mask adheres to the conventions used for AP_MASK_VALUES and DAB_MASK_VALUES
        custom_mask = self.generate_mask(mask)
        return cv2.bitwise_and(self.bgr, self.bgr, mask = custom_mask)

    def dab(self):
        ''' returns matrix representation of image including exclusively those pixels that fall in the color range specified by the mask for dab pigment '''
        dab_mask = self.generate_mask(self.DAB_MASK_VALUES)
        return cv2.bitwise_and(self.bgr, self.bgr, mask = dab_mask)

    def ap(self):
        ''' returns matrix representation of image including exclusively those pixels that fall in the color range specified by the mask for ap pigment '''
        ap_mask = self.generate_mask(self.AP_MASK_VALUES)
        return cv2.bitwise_and(self.bgr, self.bgr, mask = ap_mask)

    def dabPixelRaw(self):
        ''' return integer count of pixels that fall in the threshold of the dab pigment '''
        # TODO rename as count_dab_pixels
        return cv2.countNonZero(self.generate_mask(self.DAB_MASK_VALUES))


    def apPixelRaw(self):
        ''' return integer count of pixels that fall in the threshold of the ap pigment '''
        # TODO: rename as count_ap_pixels
        return cv2.countNonZero(self.generate_mask(self.AP_MASK_VALUES))

    def background(self): # TODO fix erosion bounds
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
