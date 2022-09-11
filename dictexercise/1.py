"""
Exercise 1: Write a program to check whether a given key exists
 in a dictionary or not.
"""
dict = {"name": "pradip", "address": "ktm", "age": 22}
check = input("Enter the key: ")

if check in dict.keys():
    print("Kye exists")
else:
    print("Key doesn't exist")
