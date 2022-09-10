
# Generators

"""
Generators are functions that return a sequence of values.
We use yield statement to return the value from function

Yield Statement

Yeild statement returns the elements
 from a generator function into a generator object

 next() function
 This function is used to
  retrive element by element from a generator object

  Syntax: next(gen_obj)
"""


def display(a, b):
    yield a  # returns the elements of a
    yield b


x, z = display(10, 20)
result = display(11, 21)
print(type(result))  # check the type of result
print(result)  # print the result i.e <generator object display at 0x0000028649559A10>
print(list(result))  # converting into list
print(x)
print(z)
