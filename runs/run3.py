from robot import Robot
from util import gyro
from pybricks.parameters import Stop, Button
from util import buttons
name = "run3"

#גמור (עובד 4 מ5 פעמים)
def start():
    while buttons.button_pressed(Button.CENTER) == False:
        if buttons.button_pressed(Button.UP):
            Robot.arm_left.run(100)
        elif buttons.button_pressed(Button.DOWN):
            Robot.arm_left.run(-100)
        else:
            Robot.arm_left.brake()
    #M04 + M01 + M14
    # "ספסל,יחידות בריאות, פרוייקט חדשנות"
    Robot.settings(straight_speed = 650)
    Robot.chassis.straight(405) 
    gyro.gyro_turn(7, 100, 1)
    Robot.chassis.straight(27)
    #מגיעים לספסל והתיישרות
    #מרימים את המשענת
    Robot.arm_left.run_angle(-200, 100)
    Robot.arm_left.run_angle(-600, 100)
    Robot.chassis.straight(5)
    gyro.gyro_turn(-3, 100, 1)
    # #מפילים את י"ב ואת הפ"ח
    # Robot.arm_right.run_angle(70, 100)
    # Robot.arm_right.run_angle(-70, 100)
    gyro.gyro_turn(-48, 100, 1)
    #Robot.arm_left.run_angle( 150, 200)

    gyro.gyro_turn(60, 100, 1)
    Robot.chassis.straight(-425)
    Robot.brake()
