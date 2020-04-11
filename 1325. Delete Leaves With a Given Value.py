# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from tree_node_lib import *
class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:

        def pre_order(root):
            ret = True
            if root == None or root.val == None:
                return True
            if root.val != target:
                ret = False
            l =  pre_order(root.left)
            if l:
                root.left = None
            r = pre_order(root.right)
            if r:
                root.right= None
            return ret and r and l
        if pre_order(root):
            return None
        return root

sol = Solution()
root = makeTree([1,1,1])
target = 1
inorder_print(sol.removeLeafNodes(root,target))