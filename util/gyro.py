from robot import Robot

<<<<<<< HEAD
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


=======
def turn_to(target, speed):
  Robot.chassis.turn(target - Robot.gyro.angle)
>>>>>>> 90750b4497dbd4e377f8bf263021a0e223505641



def follow_angle(target, distance, kp, drive_speed):
  Robot.chassis.drive(drive_speed, 0)

  while Robot.chassis.distance() < distance:
    error = target - Robot.gyro.angle()
    Robot.chassis.drive(0, error * kp)

<<<<<<< HEAD
  Robot.brake()
=======
  Robot.brake()
    
>>>>>>> 90750b4497dbd4e377f8bf263021a0e223505641
