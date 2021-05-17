from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, GyroSensor, ColorSensor
from pybricks.parameters import Port, Direction, Button
from pybricks.robotics import DriveBase
from pybricks.tools import wait

class Robot():

  #robot hardware
  brick = EV3Brick()

  wheel_left = Motor(Port.A)
  wheel_right = Motor(Port.B)

  arm_left = Motor(Port.D)
  arm_right = Motor(Port.C)

  gyro = GyroSensor(Port.S1, Direction.COUNTERCLOCKWISE)
  color_left = ColorSensor(Port.S2)
  color_right = ColorSensor(Port.S3)

  chassis = DriveBase(wheel_left, wheel_right, wheel_diameter=49.5, axle_track=150)

  @classmethod
  def reset_settings(cls):
    cls.chassis.stop()
    cls.chassis.settings(115, 460, 88, 352)

  @classmethod
  def settings(cls, 
               straight_speed=None, 
               straight_acceleration=None, 
               turn_rate=None, 
               turn_acceleration=None):
    cls.chassis.stop() #Settings can only be changed while stopped
    current_settings = cls.chassis.settings()
    cls.chassis.settings(straight_speed if straight_speed is not None else current_settings[0],
                     straight_acceleration if straight_acceleration is not None else current_settings[1],
                     turn_rate if turn_rate is not None else current_settings[2],
                     turn_acceleration if turn_acceleration is not None else current_settings[3])

  @classmethod
  def brake(cls):
    cls.chassis.stop()
    cls.wheel_left.brake()
    cls.wheel_right.brake()

  @classmethod
  def reset_gyro(cls):
    cls.gyro.reset_angle(0)

    cls.gyro.angle()
    cls.gyro.speed()
    cls.gyro.angle()
    
    wait(10)

