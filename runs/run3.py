from robot import Robot
from util import gyro
from pybricks.parameters import Stop
name = "run3"

def start():
    #M04 + M01 + M14
    # "ספסל,יחידות בריאות, פרוייקט חדשנות"
    Robot.settings(straight_speed = 650)
    Robot.chassis.straight(400) 
    gyro.gyro_turn(10, 100, 1)
    Robot.chassis.straight(25)
    #מגיעים לספסל והתיישרות
    Robot.arm_left.run_angle(-225, 100)
    Robot.chassis.straight(8)
    gyro.gyro_turn(-3, 100, 1)
    Robot.arm_right.run_angle(60, 100)
    gyro.gyro_turn(-55, 100, 1)
    Robot.arm_left.run_angle( 150, 110)

    Robot.settings(straight_speed = 750)
    gyro.gyro_turn(60, 100, 1)
    Robot.chassis.straight(-425)
    Robot.brake()
