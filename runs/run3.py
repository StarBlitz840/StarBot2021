from robot import Robot
from util import gyro
from pybricks.parameters import Stop
name = "run3"

def start():
    #M04 + M01 + M14
    # "ספסל,יחידות בריאות, פרוייקט חדשנות"
    Robot.chassis.straight(400) 
    gyro.gyro_turn(10, 100, 1)
    Robot.chassis.straight(20)
    # gyro.gyro_turn(15, 50, 1)
    #מגיעים לספסל והתיישרות
    Robot.arm_left.run_angle(-225, 100)
    gyro.gyro_turn(-55, 100, 1)
    Robot.arm_left.run_angle( 150, 110)
    Robot.arm_right.run_angle(60, 100)
    gyro.gyro_turn(-55, 100, 1)
    Robot.settings(straight_speed = 700)
    Robot.chassis.straight(500)
