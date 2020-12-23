import time
import math

def halflife(dose, half_life, timesincedose):
    ke = math.log(2)/half_life
    remaining = dose * math.pow(math.e, -ke*timesincedose)
    return remaining


# dose, half-life in seconds. Dosage remaining will update every one(1) second
# Ctrl+c to stop
def live(dose, half_life):
    try:
        time_ = 0
        ke = math.log(2)/half_life
        remaining = math.pow(math.e, -ke*0)
        while True:
            try:
                remaining = dose*math.pow(math.e, -ke*time_)
                print("Dose remaining: " + str(remaining), end='\r')
                time.sleep(1)
                time_ += 1
            except KeyboardInterrupt:
                return "Stopped live elimination counter"
    except Exception as e:
        return e
