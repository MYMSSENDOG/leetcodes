# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from tree_node_lib import *
from node_lib import *
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        list = []
        while head:
            list.append(head.val)
            head = head.next

        def helper(l,r):#l:r
            if l<r:
                mid = (r+l) // 2
                root = TreeNode(list[mid])
                root.left =helper(l,mid)
                root.right = helper(mid+1, r)
                return root

        return helper(0,len(list))

sol = Solution()
l = makeNode([-10,-3,0,5,9])
inorder_print(sol.sortedListToBST(l))