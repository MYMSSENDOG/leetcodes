# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from node_lib import *
class Solution:
    def reorderList(self, head: ListNode) -> None:
        l = 1
        cur = head
        while cur:
            cur = cur.next
            l += 1
        right = head
        for i in range((l + 1) // 2 - 1):
            right = right.next
        temp = right.next
        right.next = None
        right = temp

        last = None
        rcur = right
        while rcur:
            temp = rcur.next
            rcur.next = last
            last = rcur
            rcur = temp


        lhead = head
        rhead = last

        while rhead:
            lnext = lhead.next
            lhead.next = rhead
            lhead = lnext
            rhead, lhead = lhead, rhead
        return head

sol = Solution()
head = makeNode([1,2,3,4,5])
pr(sol.reorderList(head))
