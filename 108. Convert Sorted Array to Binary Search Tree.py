# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from tree_node_lib import *
class Solution:
    def sortedArrayToBST(self, nums) -> TreeNode:

        def helper(l,r):#l:r
            if l<r:
                mid = (r+l) // 2
                root = TreeNode(nums[mid])
                root.left =helper(l,mid)
                root.right = helper(mid+1, r)
                return root

        return helper(0,len(nums))
sol = Solution()
p = [-10,-3,0,5,9]
inorder_print(sol.sortedArrayToBST(p))
