"""Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # print(int(a, 2))
        summ =format(int(a, 2) + int(b, 2), 'b')
        return summ
sol = Solution()
print(sol.addBinary("11", "1")) #"100"