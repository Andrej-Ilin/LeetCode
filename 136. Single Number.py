"""Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:

Input: nums = [2,2,1]
Output: 1"""

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        d = []
        for i in nums:
            if i in d:
                d.remove(i)
            else:
                d.append(i)
        return d[0]



sol = Solution()
print(sol.singleNumber(nums = [2,2,1]))