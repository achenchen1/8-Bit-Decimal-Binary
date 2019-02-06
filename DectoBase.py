# Will convert a decimal number to any base less than 10
import math

def dectobase(number, base):
    if number == 0:
        print(0)
        return
    elif number < 0:
        print("-", end="")
        dectobase(-number, base)
    else:
        power = math.floor(math.log(number, base))
        for x in range(0, power+1):
            product = int(number/base**(power-x))
            print(product, end="")
            if number >= base**(power-x):
                number -= product*base**(power-x)
