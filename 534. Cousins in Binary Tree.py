# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from tree_node_lib import *
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if not root:
            return False
        q = [root]
        while q:
            X = False
            Y = False
            for node in q:
                if node.val == x:
                    X = True
                if node.val == y:
                    Y = True
            if X and Y :
                return True
            elif X or Y:
                return False

            for _ in range(len(q)):
                t = q.pop(0)
                flag = False
                if t.left:
                    if t.left.val == x or t.left.val == y:
                        flag = True
                    q.append(t.left)
                if t.right:
                    q.append(t.right)
                    if flag and (t.right.val == x or t.right.val == y):
                        return False
        return False

root = makeTree([1,2,3,None,4,None,5])
x = 4
y = 5
sol = Solution()
print(sol.isCousins(root,x,y))
