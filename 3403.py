# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from tree_node_lib import *
class Solution:
    def helper(self, inor, postor):
        if not inor or not postor:
            return None
        root = TreeNode(postor[-1])
        mid = inor.index(root.val)
        left_inor = inor[:mid]
        right_inor = inor[mid+1:]

        left_post = postor[:mid]
        right_post = postor[mid:-1]

        root.left = self.helper(left_inor, left_post)
        root.right = self.helper(right_inor, right_post)
        return root

    def buildTree(self, inorder, postorder) -> TreeNode:
        return self.helper(inorder, postorder)

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]

arr = []
sol = Solution()
inorder_print(sol.buildTree(inorder, postorder), arr)
print(arr)
