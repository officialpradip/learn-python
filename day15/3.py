"""
Return the quotient and remainder
Write a function that accepts two integers num1 and num2. 
The function should divide num1 by num2 and return 
the quotient and remainder. 
The output can be rounded to 2 decimal places.


"""


def quo_remainder(num1, num2):
    quotient = num1//num2
    result = round(quotient, 2)

    remainder = num1 % num2
    result = round(remainder, 2)
    return quotient, remainder


q, r = quo_remainder(179, 176)
print(q)
print(r)
