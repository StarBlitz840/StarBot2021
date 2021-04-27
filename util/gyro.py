from robot import Robot

def gyro_turn(angle, speed, range):
  #Robot.reset_gyro()
  start_angle = Robot.gyro.angle()
  angle += start_angle
  while abs(Robot.gyro.angle() - angle) > range:
    if angle > Robot.gyro.angle():
      Robot.chassis.drive(0, speed)
    elif angle < Robot.gyro.angle():
      Robot.chassis.drive(0, -speed)
  
  Robot.brake()


def follow_angle(target, distance, kp, drive_speed):
  Robot.chassis.reset()
  Robot.chassis.drive(drive_speed, 0)
  while Robot.chassis.distance() < distance:
    error = target - Robot.gyro.angle()
    Robot.chassis.drive(drive_speed, error * kp)

  Robot.brake()