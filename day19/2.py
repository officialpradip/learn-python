"""
Write a Python function to return all unique values in a dictionary. The values should be returned in a list.

Input Data:

input_dict = {'Box1':'Apple', 'Box2':'Mango', 'Box3':'Orange', 'Box4':'Apple', 'Box5':'Orange', 'Box6':'Orange','Box7':'Strawberry','Box8':'Apple'}

Expected outcome = ['Mango', 'Orange', 'Strawberry', 'Apple']
"""


def remove_duplicates(input_dict):
    unique_dict = list(set(input_dict.values()))
    return unique_dict


input_dict = {'Box1': 'Apple', 'Box2': 'Mango', 'Box3': 'Orange', 'Box4': 'Apple',
              'Box5': 'Orange', 'Box6': 'Orange', 'Box7': 'Strawberry', 'Box8': 'Apple'}
demo = remove_duplicates(input_dict)
print(demo)
