"""
Write a Python function to multiply all the values in a dictionary.

input_dict = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
"""


def multiply_values(input_dict):
    product = 1
    for i in input_dict:
        product = product*input_dict[i]
    return product


input_dict = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
demo = multiply_values(input_dict)
print(demo)
