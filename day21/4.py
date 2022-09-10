"""
Write a Python program to find the union of two sets.

set1 = {1,2,3,4,5}

set2 = {4,5,6,7,8}
"""


def uni(set1, set2):
    return set1.union(set2)


set1 = {1, 2, 3, 4, 5}

set2 = {4, 5, 6, 7, 8}
demo = uni(set1, set2)
print(demo)

# or


def set_union(set1, set2):
    return (set1 | set2)


a = {1, 2, 3, 4, 5}

b = {4, 5, 6, 7, 8}
demo = uni(a, b)
print(demo)
