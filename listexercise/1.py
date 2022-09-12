"""
Exercise 1: Write a program to create a list with 
random data types elements.
"""
lst = [1, 'Hello', True, 1.2]
print(lst)

for i in lst:
    print(f"{i} is of {type(i)}")

# or
for i in range(len(lst)):
    print(lst[i], type(lst[i]))
