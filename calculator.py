# https://github.com/izPilot/lab11-br-hf
# Partner 1: Hunter Fairbanks
# Partner 2: Braden Rennolds

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return b / a

def log(a, b):
    if a <= 0 or a == 1:
        raise ValueError("Logarithm base 'a' must be greater than 0 and not equal to 1.")
    if b <= 0:
        raise ValueError("Logarithm argument 'b' must be strictly positive.")
    return math.log(b, a)

def exp(a, b):
    return a ** b