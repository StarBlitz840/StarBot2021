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












  #makeing sure target_angle is positive
  # target_angle = target_angle + 360
  # target_angle = target_angle % 360

  #figuring out the direction we need to turn to
  #tuning in that diretion
  # if target_angle > Robot.gyro.angle():
  #   Robot.chassis.drive(0, speed)
  #   while Robot.gyro.angle() < target_angle:
  #     pass
  # elif target_angle < Robot.gyro.angle():
  #   Robot.chassis.drive(0, -speed)
  #   while Robot.gyro.angle() > target_angle:
  #     pass
    
  # Robot.brake()

  # angle_now = Robot.gyro.angle()
  # #if the traget is positive:
  # if target > 0:
  #   Robot.chassis.drive(0, speed)
  #   while angle_now < target:
  #     angle_now = Robot.gyro.angle()
  #     pass
  #   brake()
  # #if the target is negative:
  # else:
  #   Robot.chassis.drive(0, -speed)
  #   while angle_now > target:
  #     pass
  #   brake()





def follow_angle(target, distance, kp, drive_speed):
  Robot.chassis.reset()
  Robot.chassis.drive(drive_speed, 0)
  while Robot.chassis.distance() < distance:
    error = target - Robot.gyro.angle()
    Robot.chassis.drive(drive_speed, error * kp)

  Robot.brake()