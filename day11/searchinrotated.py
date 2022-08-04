"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
"""


class Solution(object):
    def search(self, nums, target):
        low = 0
        high = len(nums)
        while low < high:
            mid = low + (high-low)//2
            if nums[mid] == target:
                return mid
            if nums[low] <= nums[mid]:
                if target >= nums[low] and target < nums[mid]:
                    high = mid
                else:
                    low = mid+1
            else:
                if target <= nums[high-1] and target > nums[mid]:
                    low = mid+1
                else:
                    high = mid
        return -1


ob1 = Solution()
print(ob1.search([4, 5, 6, 7, 0, 1, 2], 0))
print(ob1.search([4, 5, 6, 7, 0, 1, 2], 3))
print(ob1.search([1], 0))
