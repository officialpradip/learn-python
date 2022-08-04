"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.
"""
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 1, len(nums)-1

        while l <= r:
            m = l + (r-l)//2
            if nums[m] < nums[m-1]:
                return nums[m]
            if nums[m] < nums[0]:
                r = m
            else:
                l = m + 1

        return nums[0]
    # demo = findMin(0, [3, 4, 5, 1, 2])
    # print(demo)

    # demo1 = findMin(0, [4, 5, 6, 7, 0, 1, 2])
    # print(demo1)

    # demo2 = findMin(0, [11, 13, 15, 17])
    # print(demo2)


obj1 = Solution()
print(obj1.findMin([3, 4, 5, 1, 2]))
print(obj1.findMin([4, 5, 6, 7, 0, 1, 2]))
print(obj1.findMin([11, 13, 15, 17]))
