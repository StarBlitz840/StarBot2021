from robot import Robot

BLACK = 0
WHITE = 100

#1 = right
#
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