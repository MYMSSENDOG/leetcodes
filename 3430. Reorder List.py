# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from node_lib import *
class Solution:
    def reorderList(self, head: ListNode) -> None:
        idx = []

        cur = head
        while cur:
            idx.append(cur)
            cur = cur.next
        l = 0
        r = len(idx) - 1
        left_turn = True
        while l < r:
            if left_turn:
                idx[l].next = idx[r]
                left_turn = False
                l += 1
            else:
                idx[r].next =idx[l]
                left_turn = True
                r -=1
            if l == r:
                idx[l].next = None
        return idx[0]


sol = Solution()
head = makeNode([1,2,3,4,5])
pr(sol.reorderList(head))
