from pybricks.tools import wait, StopWatch

POWER = 50

def switcher(motorD, sensor1):
    motorD.dc(-POWER)
    count = 0
    while True:
        if sensor1.distance() > 200:
            motorD.dc(-POWER)
        elif sensor1.distance() < 195:
            motorD.dc(POWER)
        else:
            break;
        
        count += 1
        if count % 3 == 0:
            print(sensor1.distance())
        wait(500)
            

    motorD.hold()
    print(sensor1.distance())

def proportional(motor, sensor, k=1, target=300):
    while True:
        if not (target - 10 <= sensor.distance() <= target):
            error = sensor.distance() - target
            motor.dc(-1 * k * error)
        else:
            motor.hold()
        
        print(sensor.distance())
        wait(10)

def pi_controller(motor, sensor, p=1, i=0, target=300):
    cum = 0
    while True:
        if not (target - 10 <= sensor.distance() <= target):
            error = sensor.distance() - target
            motor.dc(-1 * (p * error + i * cum))

            cum += error
        else:
            motor.hold()

        print(cum * i, p * error, sensor.distance(), sep=' ')
        wait(10)

def pd_controller(motor, sensor, p=1, d=0, target=300):
    watcher = StopWatch()
    is_holding = True

    old_error = 0
    while True:
        if not (target - 10 <= sensor.distance() <= target):
            error = sensor.distance() - target
            delta = error - old_error
            motor.dc(-1 * (p * error + d * delta))

            old_error = error
            is_holding = True
        else:
            motor.hold()
            if is_holding:
                print("HOLDING...", watcher.time(), sensor.distance())
                is_holding = False
            

        print(d * delta, p * error, sensor.distance(), sep=' ')
        wait(10)

def pid_controller(motor, sensor, p=1, i=0, d=0, target=300):
    watcher = StopWatch()
    is_holding = True

    cum = 0
    old_error = 0
    while True:
        if not (target - 10 <= sensor.distance() <= target):
            error = sensor.distance() - target
            delta = error - old_error
            motor.dc(-1 * (p * error + d * delta + i * cum))

            old_error = error
            cum += error

            is_holding = True

            print(p * error, i * cum, d * delta, sensor.distance(), sep=' ')
        else:
            motor.hold()
            if is_holding:
                print("HOLDING...", watcher.time(), sensor.distance())
                is_holding = False
        wait(10)
        