# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from tree_node_lib import *
class Solution:
    def binaryTreePaths(self, root: TreeNode) :
        if not root:
            return []
        ret = []
        def dfs(cur_node, path):
            if path:
                path = path + "->" + str(cur_node.val)
            else:
                path = str(cur_node.val)
            if not cur_node.left and not cur_node.right:
                ret.append(path)
                return
            if cur_node.left:
                dfs(cur_node.left, path)
            if cur_node.right:
                dfs(cur_node.right, path)
        dfs(root, "")
        return ret


root = makeTree([1,2,3,None,5])
sol = Solution()
print(sol.binaryTreePaths(root))

