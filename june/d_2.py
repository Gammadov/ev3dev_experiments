#!/usr/bin/env pybricks-micropython

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import DataLog, StopWatch, wait

ev3 = EV3Brick()
ev3.speaker.beep()

motorD = Motor(Port.D)
sensor1 = UltrasonicSensor(Port.S1)

'''
# -----------------------
data = DataLog('time', 'angle')
motorD.run(-500)
watch = StopWatch()

# Log the time and the motor angle 10 times
for i in range(10):
    # Read angle and time
    angle = motorD.angle()
    time = watch.time()

    # Each time you use the log() method, a new line with data is added to
    # the file. You can add as many values as you like.
    # In this example, we save the current time and motor angle:
    data.log(time, angle)

    # Wait some time so the motor can move a bit
    wait(100)
# -----------------------
'''

# motorD.dc(-POWER)
# count = 0
# while True:
#     if sensor1.distance() > 200:
#         motorD.dc(-POWER)
#     elif sensor1.distance() < 195:
#         motorD.dc(POWER)
#     else:
#         break;
    
#     count += 1
#     if count % 3 == 0:
#         print(sensor1.distance())
#     wait(500)
        

# motorD.hold()
# print(sensor1.distance())



ev3.speaker.beep()