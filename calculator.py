#https://github.com/gonzalezisabellaa/lab11-IG-CM.git
#Partner 1: Isabella  Gonzalez
#Partner 2: Connor Mertz

import math

def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of negative number")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if(a == 0):
        raise ZeroDivisionError("Cannot divide by zero")
    else:
        return b/a

def logarithm(a, b):
    base = a
    x = b
    if(x<=0):
        raise ValueError("Cannot take log of something less than zero")
    elif base<= 0 or base == 1:
        raise ValueError("Base must be greater than zero and not equal to one")
    else:
        return math.log(x, base)

def exp(a,b):
    return a ** b
