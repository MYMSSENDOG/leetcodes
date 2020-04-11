# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from tree_node_lib import *
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        q = [root]
        while q:
            for i in range(len(q)):
                t = q.pop(0)
                if not t.left and not t.right:
                    continue
                else:
                    t.left, t.right = t.right, t.left
                    if t.left:
                        q.append(t.left)
                    if t.right:
                        q.append(t.right)
        return root



sol = Solution()
root = makeTree([1,2,3,4,5,6,7])
inorder_print(sol.invertTree(root))
