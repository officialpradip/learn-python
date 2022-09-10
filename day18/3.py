""""
Write a Python function to remove zeroes from the below list.

input_list  = [1,2,0,9,7,0,2,6,0]
"""


def remove_zero(input_list):
    modified_input_list = [i for i in input_list if i != 0]
    return modified_input_list


input_list = [1, 2, 0, 9, 7, 0, 2, 6, 0]
demo = remove_zero(input_list)
print(demo)
