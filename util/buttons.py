from pybricks.parameters import Button
from robot import Robot

def button_pressed(btn):
    return btn in Robot.brick.buttons.pressed()

def wait_for_press(btn):
  while(not button_pressed(btn)):
    pass

  while(button_pressed(btn)):
    pass

def wait_for_any_press():
  while(not len(Robot.brick.buttons.pressed()) == 1):
    pass

  btn = Robot.brick.buttons.pressed()[0]

  while(button_pressed(btn)):
    pass

  return btn
