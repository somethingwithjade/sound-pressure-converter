# Math behind the conversions

import math

REFERENCE_PRESSURE = 2e-5  # 20 μPa

def pascal_to_db(p):
    if p <= 0:
        return None  # avoid log(0) and invalid input
    return 20 * math.log10(p / REFERENCE_PRESSURE)

def db_to_pascal(db):
    return REFERENCE_PRESSURE * 10**(db / 20)

#Describe the type of sound
def describe_db_level(db):
    if db == 0:
        return "Threshold of hearing (0 dB)"
    elif db < 10:
        return "Very soft sound (below 10 dB) — includes breathing"
    elif db < 20:
        return "Whispering at close distance"
    elif db < 35:
        return "Soft whisper or quiet room"
    elif db < 50:
        return "Quiet office / background noise"
    elif db < 65:
        return "Normal conversation / rainfall"
    elif db < 80:
        return "Traffic / vacuum cleaner"
    elif db < 100:
        return "Busy street / metro"
    elif db < 115:
        return "Shouting / loud concert"
    elif db < 130:
        return "Thunder or airplane in distance"
    else:
        return "Pain threshold / possible hearing damage"

