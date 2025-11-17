# https://github.com/gonzalezisabellaa/lab11-IG-CM.git
# Partner 1: Isabella Gonzalez
# Partner 2: Isabella Gonzalez

import math

def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of negative number")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def log(a, b):
    if a <= 0 or b <= 0 or a == 1:
        raise ValueError("Invalid log arguments")
    return math.log(b, a)

def exp(a, b):
    return a ** b
