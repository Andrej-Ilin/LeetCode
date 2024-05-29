"""You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps"""


class Solution:
    def climbStairs(self, n: int) -> int:
        assert n >= 0
        f0, f1 = 1, 1
        for i in range(n - 1):
            f0, f1 = f1, f0 + f1
        return f1


sol = Solution()
n = 2
print(sol.climbStairs(n))
