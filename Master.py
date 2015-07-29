from sr.robot import *
from front_impact_sensor import *
from token import *
from gohome import *

R = Robot()
# Your code goes here
setup_front_sensor ()
while True:
    go_to_arena