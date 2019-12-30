# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from node_lib import *

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        cur = head
        right  = None
        temp = None
        if m == n:
            return head
        for i in range(m-1):
            temp = cur
            cur = cur.next
        left = temp
        tail_left = cur
        for i in range(n-m):
            t = cur
            right = cur.next
            cur.next = temp
            cur = right
            temp = t

        tail_left.next = right.next
        right.next = temp
        if left == None:
            return right
        left.next = right

        return head

sol = Solution()
node = makeNode([1,2,3])
m = 2
n = 2
pr(sol.reverseBetween(node,m,n))
