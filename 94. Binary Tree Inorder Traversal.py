# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from tree_node_lib import *
# inorder left root right
#stack .put right root left
class Solution:
    def inorderTraversal(self, root: TreeNode) :
        ret = []
        def inorder(root):
            if root.left:
                inorder(root.left)
            ret.append(root.val)
            if root.right:
                inorder(root.right)
        inorder(root)
        return ret
sol = Solution()
tree =makeTree([1,2,3,4,5,6,])