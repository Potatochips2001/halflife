import time
import math

#dose, half-life, time since tmax
def ke(dose, half_life, timesincedose):
    ke = math.log(2)/half_life
    remaining = dose * math.pow(math.e, -ke*timesincedose)
    return remaining


# dose, half-life in seconds. Dosage remaining will update every one(1) second
# Ctrl+c to stop
def liveke(dose, half_life):
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

#dose, half-life in seconds. Dosage absorbed will update every one(1) second
# Ctrl+c to stop
def liveka(dose, half_life):
    try:
        time_ = 0
        ka = math.log(2)/half_life
        absorbed = dose - (dose * math.pow(math.e, -ka*0))
        while True:
            try:
                absorbed = dose - (dose * math.pow(math.e, -ka*time_))
                print("Dose absorbed: " + str(absorbed), end='\r')
                time.sleep(1)
                time_ += 1
            except KeyboardInterrupt:
                return "Stopped live absorption counter"
    except Exception as e:
        return e

#dose, half-life, time since dosing
def ka(dose, half_life, timesincedose):
    ka = math.log(2)/half_life
    absorbed = dose - (dose*math.pow(math.e, -ka*timesincedose))
    return absorbed

# Takes integer or float
# volume of distribution, clearance rate (eg: L/kg, L/kg/hour) units must be same (eg: ml/kg, ml/kg/hour | L/kg, L/kg/hour)
def calculate(vd, cl):
    results = math.log(2)*vd/cl
    return results
