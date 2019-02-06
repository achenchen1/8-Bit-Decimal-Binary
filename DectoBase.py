import math

def dectobase(number, base): # Will convert a number in decimal to a number in any base less than 10
    if number == 0:
        print(0)
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
                
def basetodec(number, base): # Will convert a number in any base less than 10 to decimal
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
            if number >= 10**(power-x):
                number -= product*10**(power-x)
            decimalnum+=base**(power-x)*product  
        print(decimalnum)
