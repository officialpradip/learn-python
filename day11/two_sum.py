"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order."""



from typing import List, Tuple


def twosum(nums: List[int], target: int) -> Tuple[int, int]:  # nums and target as argument
    values = {}
    for num1_index, num1 in enumerate(nums):
        num2 = target - num1  # 9-2, 6-3, 6-3 i.e 7 3 3
        try:
            num2_index = values[num2]
        except KeyError:
            values[num1] = num1_index  # 2 as it's index is 0
            # Note: Use `numtoindexmap.setdefault(num1, num1_index)` instead for lowest num1_index.
        else:
            return tuple(sorted([num1_index, num2_index]))


print(twosum([2, 7, 11, 15], 9))  # num1=2
print(twosum([3, 2, 4], 6))  # num1=3
print(twosum([3, 3], 6))
