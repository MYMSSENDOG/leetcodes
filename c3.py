from tree_node_lib import *
class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        total = [0]
        s = [0]
        M = [0]
        d = {}
        def postorder(root):
            sub_sum = root.val
            if root.left:
                sub_sum += postorder(root.left)
            total[0] += root.val
            if root.right:
                sub_sum += postorder(root.right)
            d[root] = sub_sum
            return sub_sum
        def helper(root):
            if root.left:
                helper(root.left)

            M[0] = max((s[0] - d[root]) * d[root], M[0])
            if root.right:
                helper(root.right)


        postorder(root)
        s[0] = total[0]
        total = [0]
        helper(root)
        return M[0]%(10^9 + 7.)


sol = Solution()
root = [1,2,3,4,5,6]
print(sol.maxProduct(makeTree(root)))