from robot import Robot

def turn_to(target, speed):
  Robot.chassis.turn(target - Robot.gyro)
  