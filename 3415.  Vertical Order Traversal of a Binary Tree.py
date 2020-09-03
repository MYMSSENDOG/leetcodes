# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from tree_node_lib import *
import collections
class Solution:
    def verticalTraversal(self, root: TreeNode):

        d = collections.defaultdict(list)
        q = [[0, root]]
        m, M = 1, -1
        while q:
            d2 = collections.defaultdict(list)
            for _ in range(len(q)):
                idx, cur = q.pop(0)
                m = min(m, idx)
                M = max(M, idx)
                d2[idx].append(cur.val)

                if cur.left:
                    q.append([idx - 1, cur.left])
                if cur.right:
                    q.append([idx + 1, cur.right])
            for key, val in d2.items():
                d[key] += sorted(val)
        return [d[i] for i in range(m, M + 1)]




sol = Solution()
root = makeTree([1,2,3,4,5,6,7])
print(sol.verticalTraversal(root))