"""Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).



Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2."""

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums = sorted(nums1+nums2)
        sz = len(nums)
        if sz % 2:
            return nums[sz//2]
        else:
            return (nums[sz//2] + nums[sz//2-1])/2


sol = Solution()
print(sol.findMedianSortedArrays(nums1 = [1,3], nums2 = [2,4]))
