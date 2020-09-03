# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from tree_node_lib import *
class Solution:
    def isValidSequence(self, root: TreeNode, arr) -> bool:
        if not root and not arr:
            return True
        cur = root
        q = [cur]
        for i, e in enumerate(arr):
            for _ in range(len(q)):
                t = q.pop(0)
                if t.val == e:
                    if i == len(arr) - 1 and not (t.left or t.right):
                        return True
                    if t.left:
                        q.append(t.left)
                    if t.right:
                        q.append(t.right)
            if not q:
                return False
        return False


sol = Solution()
arr = [0,0]
root = deserialize([0,1,0,0,1,0,None,None,1,0,0])
print(sol.isValidSequence(root,arr))