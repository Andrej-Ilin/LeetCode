"""
Напишите функцию, которая найдет самую длинную строку с общим префиксом среди массива строк.
Если общего префикса нет, верните пустую строку"".
"""

strs = ["flower", "flow", "flight"]


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        res = ""
        for i in zip(*strs):
            if len(set(i)) == 1:
                res += i[0]
            else:
                return res
        return res


sol = Solution()
print(sol.longestCommonPrefix(strs))
