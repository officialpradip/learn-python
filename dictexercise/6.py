"""
Exercise 7: Python program to sort dictionary by values (Ascending/ Descending).
"""
dict = {"name": 3, "address": 2, "age": 22}

val = dict.values()
print(val)
sort = sorted(val)
print(sort)

sortdes = sort[::-1]
print(sortdes)

sort_items = sorted(dict)
print(sort_items)
