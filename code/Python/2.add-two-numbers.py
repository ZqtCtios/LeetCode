# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        newList = None
        while l1 and l2:
            if not l1:
                sum = l2.val
            elif not l2:
                sum = l1.val
            else:
                sum = l1.val+l2.val
            if not newList:
                newList = ListNode(sum)
                p = newList
            else:
                q = ListNode(sum)
                p.next = q
                p = p.next
            l1 = l1.next
            l2 = l2.next
        if not l1:
            p.next = l2
        else:
            p.next = l1
        p = newList
        while p:
            if p.val >= 10:
                p.val = p.val-10
                if p.next:
                    p.next.val += 1
                else:
                    q = ListNode(1)
                    p.next = q
            p = p.next
        return newList
