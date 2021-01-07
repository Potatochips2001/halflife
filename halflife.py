import time
import math

#dose, half-life, time since tmax
def ke(dose, half_life, timesincedose):
    ke = math.log(2)/half_life
    remaining = dose * math.pow(math.e, -ke*timesincedose)
    p = 100-(1*math.pow(math.e, -ke*timesincedose)*100)
    return "Remaining {0} | Probability of elimination {1}%".format(remaining, p)


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
                p = 100-(1*(math.pow(math.e, -ke*time_))*100)
                print("Dose remaining: " + str(remaining) + " | Probability of elimination " + str(p) + "%", end='\r')
                time.sleep(0.3)
                time_ += 0.3
            except KeyboardInterrupt:
                print('\r')
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
                time.sleep(0.3)
                time_ += 0.3
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
    result = math.log(2)*vd/cl
    meanlifetime = result/math.log(2)
    constaneke = math.log(2)/result
    return "Half-life {0} | Mean-lifetime {1} | decay constant {2}".format(result, meanlifetime, constaneke)

# Initial amount, amount remaining, time after initial remaining after initial amount
def amount(initialamount, remains, timesincedose):
    result = timesincedose/math.log2(initialamount/remains)
    meanlifetime = result/math.log(2)
    constaneke = math.log(2)/result
    return "Half-life {0} | Mean-lifetime {1} | Decay constant {2}".format(result, meanlifetime, constaneke)

