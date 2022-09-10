"""
Determine the factors of a number
Write a function to determine the factors of a number. 
Return the output in the form of a list.

Example:

Input = 26

Expected output = [1,2,13,26]
"""


def factors(num):
    output_list = []
    for i in range(1, num+1):
        if num % i == 0:
            output_list.append(i)

    return output_list


result = factors(26)
print(result)
