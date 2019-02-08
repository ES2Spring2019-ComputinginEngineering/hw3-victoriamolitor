#I worked with Alexa Galuppo on this assignment.
from microbit import *
import math

def calcAx(d,e,f): #calculates the angle of tilt in the x-direction, converts it to degrees, and stores the value
    Ax = (math.atan2(d, (math.sqrt((e**2)+(f**2)))))*(180/math.pi)
    return Ax

def calcAy(g,h,i): #calculates the angle of tilt in the y-direction, converts it to degrees, and stores the value
    Ay = (math.atan2(y, (math.sqrt((x**2)+(z**2)))))*(180/math.pi)
    return Ay

def happy(j,k):
    if j <= 10 and j >= -10:
        if k <= 10 and k >= -10:
            display.show(Image.HAPPY) #when the microbit is level, a happy face is displayed on the screen
        elif k > 10:
            display.show(Image.ARROW_N) #when the microbit is pointed South, a North facing error is displayed to indicate the direction to turn the microbit to a flat level
        else:
            display.show(Image.ARROW_S) #when the microbit is tilted North, a South facing arrow is displayed, indicating the direction of tilt needed to return being level
    elif j > 10:
        if k <= 10 and k >= -10:
            display.show(Image.ARROW_W) #displays a Western arrow when the microbit is tilted East
        elif k > 10:
            display.show(Image.ARROW_NW) #displays a North-West arrow when the microbit is tilted South-East
        else:
            display.show(Image.ARROW_SW) #displays a South-West arrow when the microbit is tilted North-East
    else:
        if k <= 10 and k >= -10:
            display.show(Image.ARROW_E) #displays an Easter arrow when the microbit is tilted West
        elif k > 10:
            display.show(Image.ARROW_NE) #displays a North-East arrow when the microbit is tilted South-West
        else:
            display.show(Image.ARROW_SE) #displays a South-East arrow when the microbit is tilted North-West


while True:
    sleep(100)
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    z = accelerometer.get_z()
    a = calcAx(x,y,z)
    b = calcAy(x,y,z)
    happy(a,b)