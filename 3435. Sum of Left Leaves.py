# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from tree_node_lib import *
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:

        def helper(root, isleft):
            ret = 0
            if not root.left and not root.right and isleft:
                return root.val
            if root.left:
                ret += helper(root.left, True)
            if root.right:
                ret += helper(root.right, False)
            return ret
        if not root:
            return 0
        return helper(root, False)

sol = Solution()
root = makeTree([3,9,20,None,None,15,7])
print(sol.sumOfLeftLeaves(root))