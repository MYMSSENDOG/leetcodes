# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from tree_node_lib import *
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> int:
        if not root:
            return []
        q = [root]
        ret = []
        while q:
            cur = []
            for _ in range(len(q)):
                t = q.pop(0)
                cur.append(t.val)
                if t.left:
                    q.append(t.left)
                if t.right:
                    q.append(t.right)
            ret.insert(0, cur)
        return ret


sol = Solution()
root = makeTree([3,9,20,None,None,15,7])
print(sol.levelOrderBottom(root))