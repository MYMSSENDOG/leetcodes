# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from tree_node_lib import *
#how to solve
#똑같이 생긴 트리형태에서 r의합 l의 합 과 자신의 값을 더해 그것이 가장 크게 될 수 있는 값을 구함

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        maxi = [-99999]
        def helper(root):
            if not root:
                return 0
            l = helper(root.left)
            r = helper(root.right)
            ret = 0
            if l>0:
                ret += l
            if r>0:
                ret += r
            maxi[0] = max(maxi[0], root.val+ret)
            if root.val + ret < 0:
                return 0
            return max(0, root.val + l, root.val + r, root.val)
        helper(root)
        return maxi[0]