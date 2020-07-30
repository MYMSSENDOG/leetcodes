# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from tree_node_lib import *
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        count = [0]
        def inorder(root):
            if root.left:
                a = inorder(root.left)
                if a:
                    return a
            count[0] +=1
            if count[0] == k:
                return root.val
            if root.right:
                a = inorder(root.right)
                if a:
                    return a
        return inorder(root)


sol = Solution()
root = makeTree([3,2,4,0,None])
k = 1
print(sol.kthSmallest(root, k))