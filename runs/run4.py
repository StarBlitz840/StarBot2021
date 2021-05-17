from robot import Robot
from util import gyro
from pybricks.parameters import Stop, Button
from pybricks.tools import wait
from util import line
from util import buttons

name = "run4"

def start():
  while buttons.button_pressed(Button.CENTER) == False:
    if buttons.button_pressed(Button.UP):
      Robot.arm_left.run(100)
    elif buttons.button_pressed(Button.DOWN):
      Robot.arm_left.run(-100)
    else:
      Robot.arm_left.brake()

  Robot.reset_gyro()
  #drive forward until step counter
  gyro.follow_angle(0, 700, 1, 259)
  #driving slowly for the step counter 
  Robot.settings(straight_speed = 25)
  Robot.chassis.straight(251) 
  #driving backwards so we can turn
  Robot.settings(straight_speed = 300)
  Robot.chassis.straight(-250)
  #turning for the bridge
  Robot.chassis.drive(150, -42)
  wait(1700)
  Robot.chassis.stop()
  #line following under the bridge to get to the cubes
  line.follow_line(True, 'left', 400, 0.5, 200)
  Robot.chassis.stop()
  Robot.chassis.straight(170)
  #dropping the cubes
  Robot.arm_left.run_angle(-90, 100)
  #driving backwards, then to the dance floor
  Robot.chassis.straight(-250)
  Robot.chassis.drive(150, -42)
  wait(1000)
  Robot.chassis.stop()
  Robot.chassis.straight(400)
  #undoing what we did to drop the cubes so the arm be ready next time
  Robot.arm_left.run_angle(-100, -100)
  #going back to the dance floor
  Robot.chassis.straight(-30)
  #dancing on the dance floor
  while buttons.button_pressed(Button.CENTER) == False:
    gyro.gyro_turn(30, 50, 3)
    wait(100)
    gyro.gyro_turn(-30, 50, 3)
    wait(100)
  Robot.chassis.stop()
    # Robot.arm_left.run_angle(-60, 45)
    # gyro.gyro_turn(60, 100, 3)
    # wait(150)
    # Robot.arm_left.run_angle(-60, -45)
    # gyro.gyro_turn(60, 100, 3)
    # wait(150)