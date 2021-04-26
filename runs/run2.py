from robot import Robot
from util import gyro
from pybricks.parameters import Stop
from pybricks.tools import wait
name = "run2"

def start():
    Robot.reset_gyro()
    gyro.gyro_turn(90, 70, 1)
    wait(200)
    gyro.gyro_turn(-90, 70, 1)
    print("yoshi and yay")