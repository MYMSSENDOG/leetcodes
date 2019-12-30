# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from tree_node_lib import *
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        def helper(root):
            if not root:
                return 0
            l = helper(root.left)
            r = helper(root.right)
            if not l and not r:
                return 1
            elif r and l:
                return min(l,r) + 1
            else:
                return max(l,r) + 1

        return helper(root)

sol = Solution()
p = makeTree([-10,-3,0,5,9])
print(sol.minDepth(p))
