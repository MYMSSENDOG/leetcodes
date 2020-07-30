# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from tree_node_lib import *
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root or (not root.left and not root.right):
            return root
        else:
            root.right, root.left = self.invertTree(root.left), self.invertTree(root.right)
        return root

sol = Solution()
array = [4,2,7,1,3,6,9]
inorder_print(sol.invertTree(makeTree(array)))
"""
There is a role playing game whose main content is to break dungeon with 4-character party.

Each charater has one of three roles.

H is healer and to clear dungeon, there should be one healer

T is tanker. There should be one tanker

D is dealer. There should be TWO dealer

Every party should contain 1H, 1T, 2D



Each person has multiple characters with different role.

There are n people and role_of_characters[k] represent kth palyer's character list.

rnumber fo charcters is represented by [#of healer, #of tanker, #of dealer]

Ex)role_of_characters[k] = [5,3,3] means someone have 5 healer, 3 tanker, 3 dealer

It's guaranteed that there is at least one way that make party
"""