# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from tree_node_lib import *
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        cur = root
        parent = TreeNode(2)
        parent.left = root
        direction = "left"
        while cur and cur.val != key:
            parent = cur
            if cur.val < key:
                cur = cur.right
                direction = "right"
            elif cur.val > key:
                cur = cur.left
                direction = "left"
        if not cur:
            return root
        if not cur.left and not cur.right:
            if direction == "left":
                parent.left = None
            else:
                parent.right = None
        elif not cur.left or not cur.right:
            if direction == "left":
                parent.left = cur.left or cur.right
            if direction == "right":
                parent.right = cur.left or cur.right
        else:
            temp = cur.right
            tempp = cur
            tempd = "right"
            while temp.left:
                tempp = temp
                tempd = "left"
                temp = temp.left
            cur.val = temp.val
            if tempd == "right":
                tempp.right = None
            else:
                tempp.left = None
            if temp.right:
                if tempd == "left":
                    tempp.left = temp.right
                else:
                    tempp.right = temp.right
        if cur == root:
            return parent.left
        return root



null = None


sol = Solution()
for key in range(2, 17):
    a = []
    root = makeTree([9, 5, 13, 3, 7, 11, 15, 2, 4, 6, 8, 10, 12, 14, 16])
    inorder_print(sol.deleteNode(root, key), a)
    print(a)