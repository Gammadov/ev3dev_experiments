#!/usr/bin/env pybricks-micropython

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import wait

ev3 = EV3Brick()
ev3.speaker.beep()

motor_d = Motor(Port.D)
sensor = UltrasonicSensor(Port.S1)

POWER = 50

motor_d.dc(-POWER)
count = 0
while True:
    if sensor.distance() > 200:
        motor_d.dc(-POWER)
    elif sensor.distance() < 195:
        motor_d.dc(POWER)
    else:
        break;
    
    count += 1
    if count % 3 == 0:
        print(sensor.distance())
    wait(500)
        

# wait(1000)
motor_d.hold()
print(sensor.distance())

ev3.speaker.beep()