<<<<<<< HEAD
"""
Write a function that deletes all elements in set1 that exists only in set1 but not in set2.

set1 = {1,2,3,4,5}

set2 = {4,5,6,7,8}
"""


def diff_update(set1, set2):
    return set1.difference(set2)


a = {1, 2, 3, 4, 5}

b = {4, 5, 6, 7, 8}
demo = diff_update(a, b)
print(demo)
=======
"""
Write a function that deletes all elements in set1 that exists only in set1 but not in set2.

set1 = {1,2,3,4,5}

set2 = {4,5,6,7,8}
"""


def diff_update(set1, set2):
    return set1.difference(set2)


a = {1, 2, 3, 4, 5}

b = {4, 5, 6, 7, 8}
demo = diff_update(a, b)
print(demo)
>>>>>>> 1a00bac87b1caf73986e82aa7163b7a5abf2ceae
