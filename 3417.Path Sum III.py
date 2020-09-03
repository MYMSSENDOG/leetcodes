# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from tree_node_lib import *
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        cnt = [0]
        def helper(root):#자신이 시작인... 밑으로 내려가는 값들 중 가질 수 있는거
            ret = [0]
            if root.left:
                ret += helper(root.left)
            if root.right:
                ret += helper(root.right)
            ret = [i + root.val for i in ret]
            cnt[0] += ret.count(sum)
            return ret
        helper(root)
        return cnt[0]

null = None
root = makeTree([1])
sum = 1
sol = Solution()
print(sol.pathSum(root, sum))
