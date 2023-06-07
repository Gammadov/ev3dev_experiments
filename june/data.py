from pybricks.tools import DataLog, StopWatch, wait

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