"""
Calculate the square root of a number
Write a function that accepts a number 
and returns its square root. 
The output can be rounded to 3 decimal places.
"""
import math


def numbers(num):
    sq = math.sqrt(num)
    result = round(sq, 3)
    return result


value = numbers(7)
print(f"the square root of value is:", value)
