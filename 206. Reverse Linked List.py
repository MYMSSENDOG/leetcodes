# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from node_lib import *

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        if not head or not head.next:
            return head
        q = []
        cur = head
        while cur:
            q.append(cur)
            cur = cur.next
        t = q[-1]
        head.next = None
        for i in reversed(range(1,len(q))):
            q[i].next = q[i-1]
        return t

"""
    if not head:
        return None
    tail_head = None
    while head.next:
        cur = head
        pre = None
        while cur.next != None:
            pre = cur
            cur = cur.next

        if not tail_head:
            tail_head = cur
        else:
            tail.next = cur
        tail = cur
        pre.next = None
    tail.next = head
    head.next = None
    return tail_head
"""

sol = Solution()
head = makeNode([1,2,3,4,5])
pr(sol.reverseList(head))