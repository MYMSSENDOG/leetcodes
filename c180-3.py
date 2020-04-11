# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from tree_node_lib import *
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        ret = []
        def inorder(root):
            if root.left:
                inorder(root.left)
            ret.append(root.val)
            if root.right:
                inorder(root.right)
        def bst(left, right):
            if left == right:
                return TreeNode(ret[left])
            m = (left + right)//2
            """
            if m == left:
                cur = TreeNode(ret[left])
                cur.right = TreeNode(ret[right])
                return cur
            """
            cur = TreeNode(ret[m])
            if m > left:
                cur.left = bst(left, m-1)
            if right > m:
                cur.right = bst(m+1, right)
            return cur

        inorder(root)
        return bst(0, len(ret) - 1)

sol = Solution()
root = makeTree([1,None,2,None,3,None,4,None,None])
inorder_print(sol.balanceBST(root))