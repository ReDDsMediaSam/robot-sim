from sr.robot import *
import time

R = Robot()
# Your code goes here

R.motors[0].m0.power = 70
R.motors[0].m1.power = 70
time.sleep (2)
R.motors[0].m0.power = 0
R.motors[0].m1.power = 0

R.motors[0].m0.power = 70
R.motors[0].m1.power = -70
time.sleep (.8)
R.motors[0].m0.power = 0
R.motors[0].m1.power = 0