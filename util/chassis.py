from robot import Robot

def turn_to_chassis(target, speed):
  Robot.chassis.stop()
  ss, sa, tr, ta = Robot.chassis.settings()
  Robot.chassis.settings(ss, sa, speed, ta)
  Robot.chassis.turn(target - Robot.gyro.angle)