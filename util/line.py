from robot import Robot

BLACK = 0
WHITE = 100

#1 = right
#
def follow_line(is_right_sensor, line_side, distance, kp, drive_speed):
    target = (BLACK + WHITE) / 2
    sensor = Robot.color_right

    Robot.chassis.reset()
    Robot.chassis.drive(drive_speed, 0)

    if is_right_sensor == False:
        sensor = Robot.color_left

    while Robot.chassis.distance() <= distance:
        #when error < 0: steers to white.
        #when error > 0: steers to black.
        error = target - sensor.reflection()

        if #סטייה > target:
            #לתקן -1 * line_side
        elif #סטייה < target:
            #לתקן  1 * line_side



    #if right side sensor = right sensor
    #if right side if line mod = -1 (don't do this yet)

    #target = average of black, white

    #while not traveled distance:
    #find error
    #do turn rate of kp * error