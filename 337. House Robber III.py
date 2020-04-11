# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from tree_node_lib import *
class Solution:
    def rob(self, root: TreeNode) -> int:
        def post(root):
            l,r ,ll, lr, rr, rl = 0,0,0,0,0,0
            if root.left:
                l, ll, lr = post(root.left)
            if root.right:
                r, rl, rr = post(root.right)
            return max (l + r, root.val + ll+lr+rl+rr), l, r
        if not root:
            return 0
        return post(root)[0]

sol = Solution()
root = makeTree([3,4,5,1,3,None,1])
print(sol.rob(root))