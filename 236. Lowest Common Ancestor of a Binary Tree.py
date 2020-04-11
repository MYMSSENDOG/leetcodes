from tree_node_lib import *
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ret = []
        if not root:
            return []
        def dfs(head, route):
            if len(ret) == 2:
                return
            if head.val == p.val or head.val == q.val:
                ret.append(route)
            if head.left:
                dfs(head.left, route + "l")
            if head.right:
                dfs(head.right, route + "r")
        dfs(root, " ")
        answer = root
        i = 1
        while i <len(ret[0]) and i < len(ret[1]):
            if ret[0][i] == ret[1][i]:
                if ret[0][i] == "l":
                    answer = answer.left
                else:
                    answer = answer.right
            else:
                break
            i += 1
        return answer



sol = Solution()
root = makeTree([3,5,1,6,2,0,8,None,None,7,4])
p = makeTree([6])
q = makeTree([0])
print(sol.lowestCommonAncestor(root,p,q).val)