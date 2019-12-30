# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from tree_node_lib import *
class Solution:
    def preorderTraversal(self, root: TreeNode):

        """
        def helper(head):
            if head:
                return [head.val] + [x for x in helper(head.left)] + [y for y in helper(head.right)]
            else:
                return []
        return helper(root)
        """
        ret = []
        q = [root]
        while q:
            for i in range(len(q)):
                t = q.pop(0)
                if not t.left and not t.right:
                    ret.append(t.val)
                    continue
                q.insert(0, TreeNode(t.val))
                if t.right:
                    q.insert(0, t.right)
                if t.left:
                    q.insert(0,t.left)
        return ret




a = makeTree([1,None,2,3])
sol = Solution()
print(sol.preorderTraversal(a))