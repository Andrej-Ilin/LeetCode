"""Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go
outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
Example 1:

Input: x = 123
Output: 321
"""


class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x = 0 - int(''.join(reversed(str(x)[1:])))
            if x not in range(-2 ** 31, 2 ** 31 - 1):
                return 0
            return x
        else:
            x = int(''.join(reversed(str(x))))
            if x not in range(-2 ** 31, 2 ** 31 - 1):
                return 0
            return x
        int(''.join(reversed(str(x))))


sol = Solution()
print(sol.reverse(x=-123))
print(sol.reverse(x=1534236469))
print(sol.reverse(x=-2147483648))
