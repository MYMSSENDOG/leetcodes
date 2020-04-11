# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from tree_node_lib import *
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        def dfs(root, is_left):
            if not root.left and not root.right:
                if is_left:
                    return root.val
                else:
                    return 0
            ret = 0
            if root.left:
                ret += dfs(root.left , True)
            if root.right:
                ret += dfs(root.right, False)
            return ret
        return dfs(root, False)




sol = Solution()
root = makeTree([3,9,20,None,None,15,7])
print(sol.sumOfLeftLeaves(root))
