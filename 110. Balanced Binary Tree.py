# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from tree_node_lib import *
class Solution:
    def isBalanced(self, root: TreeNode):
        def helper(root):
            if not root:
                return 0
            l = helper(root.left)
            if l == -1:
                return-1
            r = helper(root.right)
            if r ==-1:
                return -1
            if not(-1<=l - r <=1):
                return -1
            return max(l,r) + 1
        return helper(root) != -1







sol = Solution()
p = makeTree([1,2])
print(sol.isBalanced(p))
