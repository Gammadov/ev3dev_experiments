#!/usr/bin/env pybricks-micropython

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import DataLog, StopWatch, wait

from controllers import *

ev3 = EV3Brick()
ev3.speaker.beep()

motorD = Motor(Port.D)
sensor1 = UltrasonicSensor(Port.S1)


# switcher(motorD, sensor1)
# pid_controller(motorD, sensor1, p=2, i=0.02, d=0.5)


ev3.speaker.beep()