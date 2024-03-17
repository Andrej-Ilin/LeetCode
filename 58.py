"""Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal
substring
 consisting of non-space characters only.



Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5."""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        new_str = '\n'.join(el.strip() for el in s.split('\n') if el.strip())
        return len(list(new_str.split(" ")[-1]))


sol = Solution()

print(sol.lengthOfLastWord(s="Hello World"))

