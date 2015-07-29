from sr.robot import *
import time

R = Robot()
# Your code goes here
R.motors[0].m0.power = -4
R.motors[0].m1.power = 4

def drive (speed, seconds):
     R.motors[0].m0.power = speed
     R.motors[0].m1.power = speed
     time.sleep (seconds)
     R.motors[0].m0.power = 0
     R.motors[0].m1.power = 0

def turn (speed, seconds):
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = -speed
    time.sleep (seconds)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0