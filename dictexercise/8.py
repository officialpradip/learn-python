"""
Exercise 9: Write a program to sum all the values of a dictionary.
"""
from cgitb import reset
from queue import Empty


dict = {1: 100, 2: 200}
a = dict.values()
result = sum(a)
mx = max(a)
mn = min(a)
print(result)
print(mx)
print(mn)

# check whether dict is Empty

# Dictionary is empty or not
# initialize empty dictionary
dict1 = {1: 1}

# using boolean if dictionary is empty
result = not bool(dict1)

# printing result
print("Is dictionary empty ? : " + str(result))
