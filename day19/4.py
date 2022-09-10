"""
Write a function to invert the keys and values of a dictionary.

input_dict = {'Box1':'Apple', 'Box2':'Orange'}

Expected output = {'Apple':'Box1', 'Orange':'Box2'}
"""


def invert_dict(input_dict):
    output_dict = dict(map(reversed, input_dict.items()))
    return output_dict


input_dict = {'Box1': 'Apple', 'Box2': 'Orange'}
demo = invert_dict(input_dict)
print(demo)
