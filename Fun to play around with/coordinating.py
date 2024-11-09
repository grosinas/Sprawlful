import math
import sys

def coordinating(coord): 
    x = (float(coord[0]) * 20037508.34) / 180
    y = math.log(math.tan((90 + float(coord[1])) * math.pi / 360)) / (math.pi / 180)
    y = (y * 20037508.34) / 180
    return x, y

