# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from node_lib import *
class Solution:
    def deleteNode(self, node):
        #node.val = node.next.val
        #node.next = node.next.next
        node = node.next
        pr(node)
sol = Solution()
node = makeNode([4,5,1,9])
print(sol.deleteNode(node))
