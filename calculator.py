# https://github.com/izPilot/lab11-br-hf
# Partner 1: Braden Rennolds
# Partner 2: Hunter Fairbanks

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math

def square_root(a):
    try:
        if a < 0:
            raise ValueError("Cannot calculate the square root of a negative number.")

        return math.sqrt(a)

    except ValueError as ve:
        print(f"ValueError caught: {ve}")
        return None
    except TypeError:
        print("TypeError caught: Input must be a number.")
        return None

def hypotenuse(a, b):
    try:
        return math.hypot(a, b)

    except TypeError:
        print("TypeError caught: Both inputs must be numbers.")
        return None

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return b / a

def logarithm(a, b):
    if a <= 0 or a == 1:
        raise ValueError("Logarithm base 'a' must be greater than 0 and not equal to 1.")
    if b <= 0:
        raise ValueError("Logarithm argument 'b' must be greater than 0.")
    return math.log(b, a)

def exp(a, b):
    return a ** b
