"""You are given a large integer represented as an integer array digi
integer. The digits are ordered from most significant to least signif
Increment the large integer by one and return the resulting array of

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4]

digits = [9,9]

Expected
[1,0,0]."""


class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += carry
            carry = digits[i] // 10
            digits[i] %= 10

        if carry:
            digits.insert(0, carry)

        return digits

sol = Solution()
print(sol.plusOne(digits=[1, 2, 3]))
print(sol.plusOne(digits=[4, 3, 2, 1]))
print(sol.plusOne(digits=[9, 9]))  # out [1,0,0]
