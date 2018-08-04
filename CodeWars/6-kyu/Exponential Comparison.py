import math
def compare(number1, number2):
    base1, exp1 = number1
    base2, exp2 = number2
    exp2 = exp2*math.log(base2,base1)
    return number1 if exp1>exp2 else number2