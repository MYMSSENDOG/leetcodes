# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from node_lib import *
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        cur = headA
        dict = {}
        while cur:
            dict[cur] = 1
            cur = cur.next
        cur = headB
        while cur:
            if cur in dict:
                return cur.val
            else:
                cur = cur.val
sol = Solution()
print(sol.getIntersectionNode())