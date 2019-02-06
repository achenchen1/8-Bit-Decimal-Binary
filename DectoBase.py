import math

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
        decimalnum = 0;
        power = math.floor(math.log(number, newBase))
        for x in range(0, power+1):
            product = int(number/newBase**(power-x))
            decimalnum+=product*oldBase**(power-x)
            if number >= newBase**(power-x):
                number -= product*newBase**(power-x)
        return decimalnum
        
print(basetobase(120, 6, 7))
