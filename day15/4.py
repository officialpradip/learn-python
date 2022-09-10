"""
Check whether a number is even or odd
Write a function to check whether a number is even or odd.
"""


def even_odd(num):
    if num % 2 == 0:
        return ("Even")
    else:
        return ("Odd")


numbers = even_odd(10)
print(numbers)
