# https://github.com/izPilot/lab11-br-hf
# Partner 1: Braden Rennolds
# Partner 2: Hunter Fairbanks

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

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Denominator 'a' cannot be zero.")
    return b / a

def logarithm(a, b):
    if a <= 0 or a == 1:
        raise ValueError("Logarithm base 'a' must be greater than 0 and not equal to 1.")
    if b <= 0:
        raise ValueError("Logarithm argument 'b' must be greater than 0.")
    return math.log(b, a)

def exponent(a, b):
    return a ** b