"""
Calculate the sum of three given numbers

Write a function that accepts three variables a,b,c 
and returns the sum of these variables if the values are equal 
than return two times their sum.
"""


def sum(a, b, c):
    if a == b == c:
        return 2*(a+b+c)
    else:
        return a+b+c


result = sum(1, 1, 1)
print("the result is", result)
