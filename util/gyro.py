from robot import Robot

def turn_to(target, speed):
  Robot.chassis.turn(target - Robot.gyro.angle)



def follow_angle(target, distance, kp, drive_speed):
  Robot.chassis.drive(drive_speed, 0)

  while Robot.chassis.distance() < distance:
    error = target - Robot.gyro.angle()
    Robot.chassis.drive(0, error * kp)

  Robot.brake()
    