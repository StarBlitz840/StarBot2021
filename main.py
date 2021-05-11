#!/usr/bin/env pybricks-micropython
from pybricks.parameters import Button
from util import buttons
from robot import Robot
<<<<<<< HEAD
from runs import run4, run3, run1  , motor_control

button_codes = [Button.UP, Button.RIGHT, Button.DOWN, Button.LEFT, Button.CENTER]
button_symbols = [" ^ ", " > ", " v ", " < ", "[] "]
runs = [run1, run3, run4, motor_control]
=======
from runs import run4, run3, run2, motor_control

button_codes = [Button.UP, Button.RIGHT, Button.DOWN, Button.LEFT, Button.CENTER]
button_symbols = [" ^ ", " > ", " v ", " < ", "[] "]
runs = [run2, run3, run4, motor_control]
>>>>>>> 20e300d720847147efd934a2826d2504f19b11e9

def display_menu():
  Robot.brick.screen.clear()

  for i in range(len(runs)):
    Robot.brick.screen.print(button_symbols[i] + runs[i].name)

while True:
  display_menu()

  btn = buttons.wait_for_any_press()
  btn_index = button_codes.index(btn)

  Robot.brick.screen.clear()

  Robot.reset_settings()
  runs[btn_index].start()
