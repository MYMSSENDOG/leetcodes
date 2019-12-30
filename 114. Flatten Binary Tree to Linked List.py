# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from tree_node_lib import *
class Solution:
    def flatten(self, root: TreeNode) -> None:
        if not root:
            return None
        if not root.left and not root.right:
            return root
        temp = self.flatten(root.right)
        root.right = self.flatten(root.left)
        root.left = None
        cur = root
        while cur.right:
            cur = cur.right
        cur.right = temp
        return root


sol = Solution()
p = makeTree([1,None,2,3])
inorder_print(sol.flatten(p))