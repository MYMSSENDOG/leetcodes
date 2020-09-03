# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from tree_node_lib import *
class Solution:
    def largestValues(self, root: TreeNode):

        q = [root]
        if not root:
            return []
        ret = []
        while q:
            m = -float('inf')
            for i in range(len(q)):
                t = q.pop(0)
                m = max(m, t.val)
                if t.left:
                    q.append(t.left)
                if t.right:
                    q.append(t.right)
            ret.append(m)
        return ret

sol = Solution()
root = deserialize([1,3,2,5,3,None,9])
print(sol.largestValues(root))