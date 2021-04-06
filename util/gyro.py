from robot import Robot

def gyro_turn(target, speed):
  angle_now = Robot.gyro.angle()
  #if the traget is positive:
  if target > 0:
    Robot.chassis.drive(0, speed)
    while angle_now < target:
      pass
    brake()
  #if the target is negative:
  else:
    Robot.chassis.drive(0, speed)
    while angle_now > target:
      pass
    brake()





def follow_angle(target, distance, kp, drive_speed):
  Robot.chassis.drive(drive_speed, 0)

  while Robot.chassis.distance() < distance:
    error = target - Robot.gyro.angle()
    Robot.chassis.drive(0, error * kp)

  Robot.brake()