"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.
"""

from typing import List


def maxSubArray(self, nums: List[int]) -> int:
    if max(nums) < 0:
        return max(nums)
    curr_sum, max_sum = 0, 0
    for num in nums:
        curr_sum = max(0, curr_sum + num)
        max_sum = max(curr_sum, max_sum)
    return max_sum


demo = maxSubArray(0, [-2, 1, -3, 4, -1, 2, 1, -5, 4])
print(demo)

demo1 = maxSubArray(0, [1])
print(demo1)

demo1 = maxSubArray(1, [5, 4, -1, 7, 8])
print(demo1)
