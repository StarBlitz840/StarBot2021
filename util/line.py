from robot import Robot

BLACK = 0
WHITE = 100

def drive_until_line(drive_speed)
    Robot.chassis.drive(drive_speed, 0)

    while Robot.color_left.reflection() > BLACK + 5 and Robot.color_right.reflection() > BLACK + 5:
        pass
    Robot.brake()

def follow_line(is_right_sensor, line_side, distance, kp, drive_speed):
    target = (BLACK + WHITE) / 2
    sensor = Robot.color_right
    
    if is_right_sensor == False:
        sensor = Robot.color_left

    Robot.chassis.reset()
    Robot.chassis.drive(drive_speed, 0)

    while Robot.chassis.distance() <= distance:
        #when error < 0: steers to white.
        #when error > 0: steers to black.
        error = target - sensor.reflection()

        #when following or right side
        Robot.chassis.drive(drive_speed, error)

        if line_side == "left":
            Robot.chassis.drive(drive_speed, -error)


    Robot.brake()