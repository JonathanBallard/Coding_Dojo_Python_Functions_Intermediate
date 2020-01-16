import random
import math
#Functions Intermediate I

def randInt(min=0, max=100):
    if min > max:
        return "Minimum is Larger than Maximum"
    elif max < 0:
        return "Maximum is a negative number"
    else:
        num = math.floor(random.random() * max + min)
    return num


print(randInt())
print(randInt(max=50))
print(randInt(min=50))
print(randInt(max = 500, min = 50))


























