from robot import Robot
from util import gyro
from pybricks.parameters import Stop
from pybricks.tools import wait
from util import line
from util import buttons
name = "run1"

def start():
    # Robot.chassis.drive(830, 0)
    # wait(1200)
    # Robot.chassis.stop()
    # gyro.follow_angle(100, 80, 1, 120)
    # Robot.chassis.straight(230)
    # Robot.chassis.drive(300, -85)
    # wait(1200)
    # Robot.chassis.stop()
    # Robot.chassis.straight(100)
    # Robot.arm_right.run_time(200, 3000)


    # Robot.chassis.straight(200)
    # Robot.chassis.drive(150, -42)
    # wait(1700)
    # Robot.chassis.stop()
    # line.follow_line(True, 'left', 400, 1, 100)
    # gyro.gyro_turn(-45, 50, 1)
    # Robot.chassis.straight(230)
    #Robot.arm_right.run_time(-100, 8400)
    
    Robot.reset_gyro()
    Robot.chassis.straight(200)
    Robot.chassis.drive(150, -42)
    wait(700)
    Robot.chassis.stop()
    line.follow_line(True, 'left', 770, 0.5, 150)
    Robot.chassis.stop()
    Robot.chassis.drive(220, -2)
    wait(2500)
    Robot.chassis.stop()
    wait(1000)
    Robot.arm_right.run_time(1440, 13000)
    # gyro.follow_angle(-2, 500, 1, 200)
    # Robot.chassis.stop()
    Robot.chassis.drive(-250, 2)
    buttons.wait_for_any_press()
    Robot.brake()