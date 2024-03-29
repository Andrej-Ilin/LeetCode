"""
Вам даны два непустых связанных списка, представляющих два неотрицательных целых числа. Цифры хранятся в обратном
порядке, и каждый из их узлов содержит одну цифру. Сложите два числа и верните сумму в виде связанного списка.

Вы можете предположить, что эти два числа не содержат никакого начального нуля, за исключением самого числа 0.
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
"""
l1 = [9, 9, 9, 9, 9, 9, 9]
l2 = [9, 9, 9, 9]


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse_list(head, tail=None):
        while head:
            head.next, tail, head = tail, head, head.next
        return tail
    def addTwoNumbers(self, l1: [ListNode], l2: [ListNode]) -> [ListNode]:
        l1_r = l1[::-1]
        l2_r = l2[::-1]
        summ = int("".join(map(str, l1_r))) + int("".join(map(str, l2_r)))
        summ = str(summ)
        return list(map(int, summ))[::-1]


sol = Solution()
print(sol.addTwoNumbers(l1, l2))
