# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from tree_node_lib import *
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        ret = [0]

        def preorder_traversed(root,level):
            if not root:
                return
            if ret[-1]< level:
                ret.append(level)
            preorder_traversed(root.left, level+1)
            preorder_traversed(root.right, level + 1)

        preorder_traversed(root,1)
        return ret[-1]

sol = Solution()
p = makeTree([3,9,20,5,None,None,7])
print(sol.maxDepth(p))