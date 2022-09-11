"""
Exercise 6: Python program to remove a set of keys.
"""
dict = {"name": "pradip", "address": "ktm", "age": 22}
keys_del = ["name", "age"]
dict = {k: dict[k] for k in dict.keys()-keys_del}

print(dict)
