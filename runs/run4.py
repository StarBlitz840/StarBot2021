from robot import Robot
from util import gyro
from pybricks.parameters import Stop
from pybricks.tools import wait
from util import line

name = "run4"

def start():
    Robot.reset_gyro()
    #drive forward until step counter
    gyro.follow_angle(0, 700, 1, 200)
    #driving slowly for the step counter 
    Robot.settings(straight_speed = 25)
    Robot.chassis.straight(250) 
    #driving backwards so we can turn
    Robot.settings(straight_speed = 300)
    Robot.chassis.straight(-250)
    #turning for the bridge
    Robot.chassis.drive(150, -42)
    wait(1700)
    Robot.chassis.stop()
    #line following under the bridge to get to the cubes
    line.follow_line(True, 'left', 400, 1, 200)
    Robot.chassis.stop()
    Robot.chassis.straight(170)
    #dropping the cubes
    Robot.arm_left.run_angle(-60, 100)