"Python Unique List – How to Get all the Unique Values in a List or Array"
"""
numbers = [1, 1, 2, 3, 3, 4]
unique_numbers = [1, 2, 3, 4]
"""
numbers = [1, 1, 2, 3, 3, 4]


def unique(numbers):
    unique_list = []
    unique_number = set(numbers)

    for i in unique_number:
        unique_list.append(i)
    return unique_list


print(unique(numbers))


def demo(numbers):
    unique = list(set(numbers))
    return unique


try1 = [1, 1, 1, 2, 3, 4, 5, 5, 5, 5]
result = demo(try1)
print(result)
