"""
Write a Python function to sort (ascending) a dictionary by value.

input_dict = {'apples':10,'oranges':6,'banana':12,'pears':5}

sorted_dict = {'pears': 5, 'oranges': 6, 'apples': 10, 'banana': 12}
"""


def dict_sort(input_dict):
    sorted_dict = sorted(input_dict.items(), key=lambda x: x[1])
    return sorted_dict


input_dict = {'apples': 10, 'oranges': 6, 'banana': 12, 'pears': 5}
demo = dict_sort(input_dict)
print(demo)
