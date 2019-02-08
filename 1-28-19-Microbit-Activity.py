# Megan Jenney and Ronan Gissler

from microbit import *
import math

def tilt(x, y, z):
    xdegrees = math.atan2(x, math.sqrt(y**2 + z**2)) * (180/math.pi)
    ydegrees = math.atan2(y, math.sqrt(x**2 + z**2)) * (180/math.pi)
    sleep(100)
    # display.scroll(xdegrees)
    # display.scroll(ydegrees)
    return xdegrees, ydegrees

def showing(xdegrees, ydegrees):
    if xdegrees > 5:
        if ydegrees > 5:
            display.show(Image.ARROW_NW)
        elif ydegrees < -5:
            display.show(Image.ARROW_SW)
        else:
            display.show(Image.ARROW_W)
    elif xdegrees < -5:
        if ydegrees > 5:
            display.show(Image.ARROW_NE)
        elif ydegrees < -5:
            display.show(Image.ARROW_SE)
        else:
            display.show(Image.ARROW_E)
    else:
        if ydegrees > 5:
            display.show(Image.ARROW_N)
        elif ydegrees < -5:
            display.show(Image.ARROW_S)
        else:
            display.show(Image.HAPPY)

while(True):
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    z = accelerometer.get_z()
    Ax = tilt(x, y, z)[0]
    Ay = tilt(x, y, z)[1]
    showing(Ax, Ay)
    print((Ax, Ay))
# need to include within certain constraints, i.e. within
# ranges of two sets of degrees,
# where the light will be on the microbit


# need to create function that defines where the dot image goes based
# on the tilt output range for each defined by degrees of both x and y