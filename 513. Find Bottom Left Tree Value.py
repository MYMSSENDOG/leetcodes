# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from tree_node_lib import *
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        ret = 0
        q = [root]

        while q:
            ret = q[0].val
            for i in range(len(q)):
                t = q.pop(0)
                if t.left:
                    q.append(t.left)
                if t.right:
                    q.append(t.right)
        return ret

sol = Solution()
root = deserialize([1,2,3,4,5,6,None,None,7])
print(sol.findBottomLeftValue(root))