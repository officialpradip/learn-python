"""
Python program to square each element of a list.
"""
x = [2, 3, 4, 5, 6, ""]
while("" in x):  # removing empty emelemnt
    x.remove("")
    for i in x:
        print(i*2, end=" ")
