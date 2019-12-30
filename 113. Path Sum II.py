# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from tree_node_lib import *
class Solution:
    def pathSum(self, root: TreeNode, sum: int):
        ret  = []
        def helper(root,sum,array):
            if not root:
                return
            array.append(root.val)
            if not root.left and not root.right and root.val == sum:
                ret.append(array[:])
            else:
                helper(root.left, sum - root.val, array)
                helper(root.right, sum - root.val, array)
            array.pop(-1)
        helper(root,sum,[])
        return ret
sol = Solution()
p = makeTree([5,4,8,11,None,13,4,7,2,None,None,5,1])
sum = 22
print(sol.pathSum(p, sum))
