# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from tree_node_lib import *
class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:

        """ 만약 preorder 가 아니라 levelorder이면 이게 맞는듯 하다 .
        if not preorder:
            return None
        mid = inorder.index(preorder[0])
        inorder_left = inorder[0:mid]
        inorder_right = inorder[mid+1:]
        preorder_left = []
        preorder_right = []
        root = TreeNode(preorder[0])
        for i in preorder[1:]:
            if i in inorder_left:
                preorder_left.append(i)
            else:
                preorder_right.append(i)

        root.left = self.buildTree(preorder_left,inorder_left)
        root.right = self.buildTree(preorder_right,inorder_right)
        return root
        """

        inddic = {val: i for i, val in enumerate(inorder)}
        def helper(l, r):
            if l<r:
                root = TreeNode(preorder.pop(0))
                mid = inddic[root.val]

                root.left = helper(l,mid)
                root.right = helper(mid+1,r)
                return root
        return helper(0,len(inorder))
sol = Solution()
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
#[3,9,20,None,None,15,7]
inorder_print(sol.buildTree(preorder,inorder))
