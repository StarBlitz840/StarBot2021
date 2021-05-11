from robot import Robot
from pybricks.parameters import Button

name = "motor control"

motors = [Robot.wheel_left, Robot.wheel_right, Robot.arm_left, Robot.arm_right]
toggled = False
speed = 360 * 4

def start():
  global toggled
  display()
  while True:
    btns = Robot.brick.buttons.pressed()
    
    if Button.UP in btns:
      motors[get_state()].run(speed)
    elif Button.DOWN in btns:
      motors[get_state()].run(-speed)
    else:
      motors[get_state()].stop()

    if Button.RIGHT in btns:
      motors[get_state() + 1].run(speed)
    elif Button.LEFT in btns:
      motors[get_state() + 1].run(-speed)
    else:
      motors[get_state() + 1].stop()

    if Button.CENTER in btns:
      toggled = not toggled
      display()


def get_state():
  global toggled
  return int(toggled) * 2

def display():
  Robot.brick.screen.clear()
  if not toggled:
    Robot.brick.screen.print("^/v  left wheel")
    Robot.brick.screen.print(">/<  right wheel")
  else:
    Robot.brick.screen.print("^/v  left arm")
    Robot.brick.screen.print(">/<  right arm")