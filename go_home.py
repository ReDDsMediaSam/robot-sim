from sr.robot import *
import time

TURN_TIME = 4
TURN_SPEED = 40

R = Robot()
# Your code goes here
print "started code"
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

def go_to_home(arena_marker_number, ANGLE_SEARCH=4):
    running = True
    while running:
        markers = R.see()
        for m in markers:
            print "Marker angle is", m.rot_y
            print "Angle seaching is", ANGLE_SEARCH
            if m.info.marker_type == MARKER_ARENA and m.info.offset == arena_marker_number and m.rot_y >=-ANGLE_SEARCH and m.rot_y <=ANGLE_SEARCH:
                drive (70, 1)
                if m.rot_y <-ANGLE_SEARCH:
                    turn(TURN_SPEED, TURN_TIME)
                elif m.rot_y >ANGLE_SEARCH:
                    turn(-TURN_SPEED, TURN_TIME)
                ANGLE_SEARCH += 1
            if m.info.marker_type == MARKER_ARENA and m.info.offset == arena_marker_number and m.dist <= 1:
                R.motors[0].m0.power = 0
                R.motors[0].m1.power = 0
                running = False
"""R.zone

d = {
0: [0, 1, 27, 26]
1: [5, 6, 7, 8]
2: [12, 13, 14, 15]
3: [19, 20, 21, 22]
}

my_zone = d[R.zone]"""
def setup_sensors ():
    R.ruggeduinos[0].pin_mode(3, INPUT)
    R.ruggeduinos[0].pin_mode(4, INPUT)
    R.ruggeduinos[0].pin_mode(5, INPUT)
def sensors ():
    pin3 = R.ruggeduinos[0].digital_read(3)
    pin4 = R.ruggeduinos[0].digital_read(4)
    pin5 = R.ruggeduinos[0].digital_read(5)
    if pin3:
        R.servos[0][0] = -80
        R.servos[0][1] = 80

    elif pin4 is False:
        print "Servo 2"
        R.motors[0].m0.power = -30
        R.motors[0].m1.power = -30
        time.sleep (.2)
        R.motors[0].m0.power = -30
        R.motors[0].m1.power = 30
        time.sleep (.4)
        R.motors[0].m0.power = 0
        R.motors[0].m1.power = 0

    elif pin5 is False:
        print "Servo 3"
        R.motors[0].m0.power = 30
        R.motors[0].m1.power = 30
        time.sleep (.2)
        R.motors[0].m0.power = -30
        R.motors[0].m1.power = 30
        time.sleep (.4)
        R.motors[0].m0.power = 0
        R.motors[0].m1.power = 0

setup_sensors()
while True:
    sensors()


