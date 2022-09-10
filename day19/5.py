"""
Write a Python script to generate 
and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
"""
n = int(input("Input a number "))
d = dict()

for x in range(1, n+1):
    d[x] = x*x

print(d)


def create_dict():
    n = 1
    d = dict()
    for x in range(1, n+1):
        d[x] = x*x
    return d
