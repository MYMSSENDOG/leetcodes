# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from tree_node_lib import *
class Solution:
    def levelOrderBottom(self, root: TreeNode) :
        ret = []
        def helper(root,level):
            if not root:
                return
            if level>len(ret):
                ret.insert(0,[root.val])
            else:
                ret[-level].append(root.val)
            helper(root.left,level+1)
            helper(root.right, level + 1)
        helper(root,1)
        return ret

sol = Solution()
p = makeTree([3,9,20,5,None,None,7])
print(sol.levelOrderBottom(p))