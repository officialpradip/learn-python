"""
Exercise 5: Write a program in python to map 2 lists into a dictionary.
"""
keys = [1, 2, 3]
values = ['v1', 'v2', 'v3', 'v4']

result_lst = list(zip(keys, values))
result_dict = dict(zip(keys, values))
print(result_lst)
print(result_dict)
