from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, GyroSensor, ColorSensor
from pybricks.parameters import Port, Direction, Button
from pybricks.robotics import DriveBase
from pybricks.tools import wait

class Robot():

  #robot hardware
  brick = EV3Brick()

  wheel_left = Motor(Port.B)
  wheel_right = Motor(Port.C)

  arm_left = Motor(Port.A)
  arm_right = Motor(Port.D)

  gyro = GyroSensor(Port.S1, Direction.CLOCKWISE)
  color_left = ColorSensor(Port.S2)
  color_right = ColorSensor(Port.S3)

  chassis = DriveBase(wheel_left, wheel_right, wheel_diameter=49.5, axle_track=150)
 
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

