# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from tree_node_lib import *

class Solution:
    def rightSideView(self, root: TreeNode) :
        ret = []
        cur = root
        q = [root]
        while q:
            size = len(q)
            s = 0
            for i in range(len(q)):
                s +=1
                t = q.pop(0)
                if s == size:
                    ret.append(t.val)
                if t.left:
                    q.append(t.left)
                if t.right:
                    q.append(t.right)

        return ret

sol = Solution()
root = makeTree([1,2,3,None,5,None,4])
print(sol.rightSideView(root))