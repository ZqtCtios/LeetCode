# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        sum = 0
        l = []
        while head:
            x = head.val
            l = [x]+l
            head = head.next
        for i in range(len(l)):
            if l[i] == 1:
                sum += pow(2, i)
        return sum
