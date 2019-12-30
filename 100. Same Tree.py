# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from tree_node_lib import *
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not q and not p:
            return True
        elif not q or not p:
            return False

        if p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)


sol = Solution()
p = makeTree([1,3,None,None,2])
q = makeTree([1,3,None,None,2])
print(sol.isSameTree(p,q))
