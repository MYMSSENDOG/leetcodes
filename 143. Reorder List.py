# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from node_lib import *
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        q = []
        cur =head
        while cur:
            q.append(cur)
            cur = cur.next
        q.pop(0)
        cur =head
        while q:
            t = q.pop(-1)
            cur.next = t
            cur = cur.next
            if q:
                t = q.pop(0)
                cur.next = t
                cur = cur.next
        cur.next = None
        return head