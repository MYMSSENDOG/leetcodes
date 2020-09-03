# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from tree_node_lib import *
class Solution:
    def bstFromPreorder(self, preorder) -> TreeNode:
        def helper(array):
            if len(array) == 1:
                return TreeNode(array[0])
            elif not array:
                return None
            else:
                cur = TreeNode(array[0])

                lstart = len(array)
                rstart = len(array)

                if array[0] > array[1]:
                    lstart = 1
                for i in range(1,len(array)):
                    if array[i] > array[0]:
                        rstart = i
                        break
                l = helper(array[lstart:rstart])
                r = helper(array[rstart:])
                cur.left = l
                cur.right = r
                return cur
        return helper(preorder)

sol = Solution()

preorder = [8,5,1,7,10,12]
print(serialize(sol.bstFromPreorder(preorder)))