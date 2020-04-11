# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from node_lib import *
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1.val == 0 and l2.val == 0:
            return ListNode(0)
        lv1 = 0
        cur = l1
        while cur:
            lv1 *= 10
            lv1 += cur.val
            cur = cur.next
        lv2 = 0
        cur = l2
        while cur:
            lv2 *= 10
            lv2 += cur.val
            cur = cur.next
        s = str(lv1 + lv2)
        ret = None
        prev = None
        for c in s:
            if not ret:
                ret = ListNode(int(c))
                prev = ret
            else:
                prev.next = ListNode(int(c))
                prev = prev.next
        return ret


sol = Solution()
l1 = makeNode([7,8,1,5])
l2 = makeNode([5,9,9])
print(sol.addTwoNumbers(l1, l2))