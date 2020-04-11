# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from node_lib import *
class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next

sol = Solution()
node = makeNode([4,5,1,9])
n = 5
sol.deleteNode(node,n)
pr(node)