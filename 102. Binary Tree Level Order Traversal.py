# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from tree_node_lib import *
from collections import deque
import queue
class Solution:
    def levelOrder(self, root: TreeNode):
        ret = []
        def preorder_traversed(root,level):
            if not root:
                return
            if len(ret) < level:
                ret.append([])
            ret[level-1].append(root.val)
            preorder_traversed(root.left, level+1)
            preorder_traversed(root.right, level + 1)

        preorder_traversed(root,1)
        return ret


sol = Solution()
p = makeTree([3,9,20,5,None,None,7])
print(sol.levelOrder(p))