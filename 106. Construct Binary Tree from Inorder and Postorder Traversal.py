# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from tree_node_lib import *
class Solution:
    def buildTree(self, inorder, postorder) -> TreeNode:

        inddic = {val:i for i, val in enumerate(inorder)}
        def helper(l,r):
            if l<r:
                root = TreeNode(postorder.pop(-1))
                mid = inddic[root.val]
                root.right = helper(mid + 1, r)
                root.left = helper(l,mid)
                return root
        return helper(0,len(inorder))
sol = Solution()
postorder = [9,15,7,20,3]
inorder = [9,3,15,20,7]
inorder_print(sol.buildTree(inorder,postorder))
