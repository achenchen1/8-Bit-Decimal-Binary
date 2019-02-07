import math
import sys

def dectobase(number, base):
    if number == 0:
        print(0)
    elif number < 0:
        print("-", end="")
        dectobase(-number, base)
    else:
        displaynum = 0
        power = math.floor(math.log(number, base))
        for x in range(0, power+1):
            product = int(number/base**(power-x))
            displaynum+=product*10**(power-x)
            if number >= base**(power-x):
                number -= product*base**(power-x)
        return displaynum

def basetodec(number, base):
    if number == 0:
        print(0)
    elif number < 0:
        print("-", end="")
        basetodec(-number, base)
    else:
        decimalnum = 0;
        power = math.floor(math.log(number, 10))
        for x in range(0, power+1):
            product = int(number/10**(power-x))
            decimalnum+=product*base**(power-x)
            if number >= 10**(power-x):
                number -= product*10**(power-x)
        return decimalnum

def basetobase(number, oldBase, newBase): #does not yet work
    if number == 0:
        print(0)
    elif number < 0:
        print("-", end="")
        basetobase(-number, oldBase, newBase)
    else:
        return dectobase(basetodec(number, oldBase), newBase)

def printdectobase(bits, number, base):
    if(number >= base**bits):
        sys.exit("Not enough bits!")
    if number == 0:
        for x in range (0, bits):
            print(0)
    elif number < 0:
        print("-", end="")
        dectobase(-number, base)
    else:
        displaynum = 0
        power = math.floor(math.log(number, base))
        for x in range(0, bits-(power+1)):
            print(0, end="")
        for x in range(0, power+1):
            product = int(number/base**(power-x))
            print(product, end="")
            if number >= base**(power-x):
                number -= product*base**(power-x)
