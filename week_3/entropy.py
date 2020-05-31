import math
def entropy(proArray):
    entropy = 0
    for i in proArray:
        entropy+= i*(math.log(float(i),2.0))
    return entropy