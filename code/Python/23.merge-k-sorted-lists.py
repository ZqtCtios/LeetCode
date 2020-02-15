# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        a = []
        for root in lists:
            p = root
            while p:
                a.append(p.val)
                p = p.next
        a.sort()
        res = ListNode(0)
        p = res
        for x in a:
            q = ListNode(x)
            p.next = q
            p = p.next
        return res.next
