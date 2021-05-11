from robot import Robot
from util import gyro
from pybricks.parameters import Stop
from pybricks.tools import wait
name = "run1"

def start():
    Robot.chassis.drive(830, 0)
    wait(1200)
    Robot.chassis.stop()
    gyro.follow_angle(100, 80, 1, 120)
    Robot.chassis.straight(230)
    Robot.chassis.drive(300, -85)
    wait(1200)
    Robot.chassis.stop()
    Robot.chassis.straight(100)

