from robot import Robot
from util import gyro
from pybricks.parameters import Stop
name = "run3"

def start():
    # M04+M01+M14
    Robot.chassis.straight(450)
    gyro.gyro_turn(20, 50, 1)
    Robot.arm_right.run_angle( 150, 100, then=Stop.HOLD, wait = True)
    gyro.gyro_turn(55, 100, 1)
    Robot.arm_right.run_angle( 150, -110, then=Stop.HOLD, wait = True)
    gyro.gyro_turn(-55, 100, 1)
    Robot.chassis.straight(-500)
