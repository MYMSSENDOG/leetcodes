# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from tree_node_lib import *
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        ret = [0]
        def helper(root):
            if not root:
                return None
            a = helper(root.left)
            if a != None:
                return a
            ret[0] += 1
            if ret[0] == k:
                return root.val

            a = helper(root.right)
            if a != None:
                return a
        return helper(root)


sol = Solution()
root = makeTree([3,1,4,None,2])
k = 2
print(sol.kthSmallest(root,k))