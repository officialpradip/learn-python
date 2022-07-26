"""
Write a function that accepts 2 strings (first_name, last_name). 
The function should concatenate these two strings by inserting a space 
in between the strings and then reverse the resultant string.

Example:

first_name = 'Allen'

last_name  = 'Brown'

Expected output = 'nworB nellA'
"""


def string_reverse(first_name, last_name):
    demo = first_name + " " + last_name
    result = demo[::-1]
    return result


res = string_reverse('Allen', 'Brown')
print(res)
