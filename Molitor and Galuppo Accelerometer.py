from microbit import *
import math

def calcAx(d,e,f): #calculates the angle of tilt in the x-direction
    Ax = (math.atan2(d, (math.sqrt((e**2)+(f**2)))))*(180/math.pi)
    return Ax

def calcAy(g,h,i): #calculates the angle of tilt in the y-direction
    Ay = (math.atan2(y, (math.sqrt((x**2)+(z**2)))))*(180/math.pi)
    return Ay

def happy(j,k):
    if j <= 10 and j >= -10:
        if k <= 10 and k >= -10:
            display.show(Image.HAPPY)
        elif k > 10:
            display.show(Image.ARROW_N)
        else:
            display.show(Image.ARROW_S)
    elif j > 10:
        if k <= 10 and k >= -10:
            display.show(Image.ARROW_W)
        elif k > 10:
            display.show(Image.ARROW_NW)
        else:
            display.show(Image.ARROW_SW)
    else:
        if k <= 10 and k >= -10:
            display.show(Image.ARROW_E)
        elif k > 10:
            display.show(Image.ARROW_NE)
        else:
            display.show(Image.ARROW_SE)


while True:
    sleep(100)
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    z = accelerometer.get_z()
    a = calcAx(x,y,z)
    b = calcAy(x,y,z)
    print((a, b))
    happy(a,b)


#Use conditionals to specify what is displayed on the microbit

#example
#if((tiltX <=10) and (tiltY <=10)):
    #display level