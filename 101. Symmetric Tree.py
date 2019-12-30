# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from tree_node_lib import *
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        def same(left, right):
            if not left and not right:
                return True
            elif  not(left and right):
                return False
            if left.val != right.val:
                return False
            else:
                return same(left.left, right.right) and same(left.right, right.left)
        return same(root.left, root.right)



sol = Solution()
p = makeTree([1,2,2,3,4,4,3])
print(sol.isSymmetric(p))