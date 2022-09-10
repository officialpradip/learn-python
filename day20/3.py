"""
Write a Python function to remove duplicates from Dictionary.

Input data:

input_dict            =  {'Box1':'Apple', 'Box2':'Mango', 'Box3':'Orange', 'Box4':'Apple', 'Box5':'Orange', 'Box6':'Orange','Box7':'Strawberry','Box8':'Apple'}

Expected output =   {'Box2': 'Mango', 'Box6': 'Orange', 'Box7': 'Strawberry', 'Box8': 'Apple'}
"""


def remove_duplicates(input_dict):
    modified_input_dict = dict(set(input_dict.items()))
    return modified_input_dict


input_dict = {'Box1': 'Apple', 'Box2': 'Mango', 'Box3': 'Orange', 'Box4': 'Apple',
              'Box5': 'Orange', 'Box6': 'Orange', 'Box7': 'Strawberry', 'Box8': 'Apple'}
demo = remove_duplicates(input_dict)
print(demo)
