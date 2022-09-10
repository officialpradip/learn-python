"""
Write a Python function that returns the maximum value in a dictionary.

input_dict = {1:1, 2:4, 3:9, 4:16, 5:25}
"""


def max_value(input_dict):
    result = max(input_dict.values())
    return result


input_dict = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
demo = max_value(input_dict)
print(demo)
