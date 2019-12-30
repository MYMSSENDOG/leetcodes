# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from tree_node_lib import *
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        q = [[root,root.val]]
        ret = 0
        while q:
            for i in range(len(q)):
                t = q.pop(0)
                cur = t[0]
                cur_val = t[1]
                if cur.left:
                    q.append([cur.left, 10*cur_val + cur.left.val])
                if cur.right:
                    q.append([cur.right, 10*cur_val + cur.right.val])
                elif not cur.left:
                    ret += cur_val
                    print(cur_val )
        return ret


sol = Solution()
array = [1,2,3,4,5]
root = makeTree(array)
print(sol.sumNumbers(root))