"""Given two integers dividend and divisor, divide two integers without using multiplication, division,
and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345
would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = 3.33333.. which is truncated to 3."""


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        result = int(dividend/divisor)
        if result >= 2147483648:
            return 2147483647
        return result

sol = Solution()
print(sol.divide(dividend = -2147483648, divisor = -1)) #2147483647
print(sol.divide(dividend = 10, divisor = 3)) # 3