# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = Nonea
from node_lib import *
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head :
            return None
        cur = head
        start = cur
        tail = cur
        cur = cur.next
        while cur!=None:
            if tail.val != cur.val:
                tail.next = cur
                tail = cur
            else:
                pass
            cur = cur.next
        tail.next = None
        pr(start)


sol = Solution()
n = makeNode([1, 1, 2,3,3,4,5,5,6,6,6,7])
print(sol.deleteDuplicates(n))