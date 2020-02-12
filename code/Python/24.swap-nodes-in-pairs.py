# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        p = head
        q = head.next
        head = q
        p.next = q.next
        head.next = p
        p = head.next.next
        c = head.next
        while p and p.next:
            q = p.next
            p.next = q.next
            c.next = q
            q.next = p
            c = p
            p = p.next
        return head
