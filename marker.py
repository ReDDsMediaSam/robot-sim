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

def go_to(arena_marker_number, ANGLE_SEARCH=4):
    running = True
    while running:
        markers = R.see()
        for m in markers:
            print "Marker angle is", m.rot_y
            print "Angle seaching is", ANGLE_SEARCH
            if m.info.marker_type == MARKER_ARENA and m.info.offset == arena_marker_number and m.rot_y >=-ANGLE_SEARCH and m.rot_y <=ANGLE_SEARCH:
                drive (70, 0.2)
                if m.rot_y <-ANGLE_SEARCH:
                    turn(TURN_SPEED, TURN_TIME)
                elif m.rot_y >ANGLE_SEARCH:
                    turn(-TURN_SPEED, TURN_TIME)
                ANGLE_SEARCH += 1
            if m.info.marker_type == MARKER_ARENA and m.info.offset == arena_marker_number and m.dist <= 1:
                R.motors[0].m0.power = 0
                R.motors[0].m1.power = 0
                running = False