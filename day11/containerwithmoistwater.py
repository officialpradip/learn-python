"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container
"""
from typing import List


class Solution:
    def maxArea(self, H: List[int]) -> int:
        ans, i, j = 0, 0, len(H)-1
        while (i < j):
            if H[i] <= H[j]:
                res = H[i] * (j - i)
                i += 1
            else:
                res = H[j] * (j - i)
                j -= 1
            if res > ans:
                ans = res
        return ans


obj = Solution()
print(obj.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(obj.maxArea([1, 1]))


# explaination:https://dev.to/seanpgallivan/solution-container-with-most-water-1907
