"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""
from typing import List


# def productExceptSelf(self, nums: List[int]) -> List[int]:
#     start, end, n = 1, 1, len(nums)
#     out = [1]*n
#     for i in range(n):
#         out[i] *= start
#         start *= nums[i]
#         out[~i] *= end
#         end *= nums[~i]
#     return out

def productExceptSelf(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    before = [1]*len(nums)  # replacing all nums value with one
    after = [1]*len(nums)
    product = [0]*len(nums)  # replacing with 0

    for i in range(1, len(nums)):
        before[i] = before[i-1]*nums[i-1]

    for i in range(len(nums)-2, -1, -1):
        after[i] = after[i+1]*nums[i+1]

    for i in range(0, len(nums)):
        product[i] = before[i]*after[i]

    return product


demo = productExceptSelf(0, [1, 2, 3, 4])
print(demo)

demo1 = productExceptSelf(0, [-1, 1, 0, -3, 3])
print(demo1)
