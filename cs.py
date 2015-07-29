from sr.robot import *
buttonPin = 3
R = Robot()
# Your code goes here
def setup ():
    R.ruggeduinos[0].pin_mode(buttonPin, INPUT)
def arm_movement ():
    pin3 = R.ruggeduinos[0].digital_read(buttonPin)
    if pin3:
        R.servos["0WW24"][1] = -40
    else:
        R.servos["0WW24"][1] = 0
