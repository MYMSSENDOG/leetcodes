from tree_node_lib import *
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        s = min(p.val, q.val)
        b = max(p.val, q.val)
        cur = root
        while not s<=cur.val<=b:
            if cur.val<s:
                cur = cur.right
            elif cur.val>b:
                cur = cur.left
        return cur




sol = Solution()
root = makeTree([6,2,8,0,4,7,9,None,None,3,5])
print(sol.lowestCommonAncestor(root))