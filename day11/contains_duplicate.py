"""
Given an integer array nums,
return true if any value appears at least twice in the array, and return false if every element is distinct
"""
from typing import List


def containsDuplicate(nums: List[int]) -> bool:  # -> annotate return value
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            return True
    return False


result1 = containsDuplicate([1, 2, 3, 1])
print(result1)

result2 = containsDuplicate([1, 2, 3, 4])
print(result2)

result3 = containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
print(result3)
