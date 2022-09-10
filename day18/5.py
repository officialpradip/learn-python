"""
Write a Python function to sum all the values in a dictionary and return the total value.

input_dict = {'a':100,'b':-54,'c':247}
"""


def sum_values(input_dict):
    total_value = sum(input_dict.values())

    return (total_value)


input_dict = {'a': 100, 'b': -54, 'c': 247}
demo = sum_values(input_dict)
print(demo)
