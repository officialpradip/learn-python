"""
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.
"""
from typing import List


def maxProduct(self, nums: List[int]) -> int:
    maxSub = nums[0]
    minSub = nums[0]
    result = nums[0]

    for i in range(1, len(nums)):
        curr = nums[i]

        tempMax = max(curr, maxSub * curr, minSub * curr)
        minSub = min(curr, maxSub * curr, minSub * curr)

        maxSub = tempMax

        result = max(maxSub, result)

    return result


demo1 = maxProduct(0, [2, 3, -2, 4])
print(demo1)

demo2 = maxProduct(0, [-2, 0, -1])
print(demo2)
