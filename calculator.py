# https://github.com/Avasius-Prime/lab11-TG-SN.git
# Partner 1: Timothy Giles (did not participate)
# Partner 2: Selasi Nukunya

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0: # raise ZeroDivisionError if a == 0
        raise ZeroDivisionError
    else:
        return b / a

def logarithm(a, b):
    if a <= 1 or b <= 0:
        raise ValueError
    else:
        return math.log(b, a) # use math library + raise ValueError

def exp(a, b):
    return a^b

def hypotenuse(a, b):
    return math.sqrt((a^2) + (b^2))

def square_root(a):
    if a < 0:
        raise ValueError
    else:
        return math.sqrt(a)