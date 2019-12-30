# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from node_lib import *
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None
        cur = head
        dict = {cur: 0}
        i = 1
        while cur.next:
            cur = cur.next
            if cur in dict:
                return cur
            else:
                dict[cur] = i

        return None

