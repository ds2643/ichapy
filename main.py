# main module of immunohistochemistry analysis tool

import math
import os
import csv # TODO not in use; incorperate csv output functionality
import sys
import imageprocessing as ip

if __name__ == "__main__":
    if len(sys.argv) > 1:
        path = "./" + sys.argv[1]
    else:
        print("A directory must be specified. Using provided data as default")
        path = "./data"
    files = [str(filename) for filename in os.listdir(path)]
    count = []
    for filename in os.listdir(path):
        if filename.endswith("png"):
            # TODO incorperate controls into cli by flag
            a = ip.Slide("./images/" + filename)
            a.dab()
            b = ip.Contour(a.dab(),filename)
            print("cells counted for file " + filename + " = " + str(b.cellCount()))
