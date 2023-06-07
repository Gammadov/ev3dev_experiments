from pybricks.tools import wait

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