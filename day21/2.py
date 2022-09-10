"""
Write a Python program to find the intersection of two sets.

set1 = {1,2,3,4,5}

set2 = {4,5,6,7,8}
"""


def inter(set1, set2):
    result = set1.intersection(set2)
    return result


set1 = {1, 2, 3, 4, 5}

set2 = {4, 5, 6, 7, 8}
demo = inter(set1, set2)
print(demo)
