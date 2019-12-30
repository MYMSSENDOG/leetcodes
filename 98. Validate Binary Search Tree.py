from tree_node_lib import *

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        t = []
        def inorder_traverse(head):
            if head.left:
                inorder_print(head.left)
            t.append(head.val)
            if head.right:
                inorder_print(head.right)
        for i in range(1,len(t)):
            if t[i] < t[i-1]:
                return False
        return True
sol = Solution()
n = makeTree([5,1,4,None,None,3,6])
print(sol.isValidBST(n))