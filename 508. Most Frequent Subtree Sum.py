# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from tree_node_lib import *
import collections
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) :
        d = collections.defaultdict(int)
        def dfs(root):
            if not root:
                return 0
            if not root.left and not root.right:
                d[root.val] +=1
                return root.val
            l = dfs(root.left)
            r = dfs(root.right)
            d[l+r+root.val] +=1
            return l+r+root.val
        dfs(root)
        m = 0
        ret = []
        for i, e in d.items():
            if e > m:
                ret = [i]
                m = e
            elif e == m:
                ret.append(i)
        return ret



sol = Solution()
root = deserialize([5,2,-3])
print(sol.findFrequentTreeSum(root))
