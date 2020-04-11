# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from node_lib import *
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return None

        while head and head.val == val:
            head = head.next
        prev = head
        if not head:
            return 
        cur = head.next
        while cur:
            if cur.val == val:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        return head

sol = Solution()
head = makeNode([1])
val = 1
pr(sol.removeElements(head,val))