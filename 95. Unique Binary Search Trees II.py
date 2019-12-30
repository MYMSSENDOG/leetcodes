from tree_node_lib import *

class Solution:
    def generateTrees(self, n: int) :
        a = [0]*n
        for i in range(n):
            a[i] = i+1
        if n == 0:
            return[]
        def maker( array ):
            n = len(array)
            ret = []
            if n == 0:
                return [None]
            elif n == 1:
                return [TreeNode(array[0])]
            ret = []
            for i in range(n):
                for l in maker(array[:i]):
                    for r in maker(array[i+1:]):
                        mid = TreeNode(array[i])
                        mid.left = l
                        mid.right = r
                        ret+= [mid]
            return ret
        return maker(a)
sol = Solution()
n = 0
for i in (sol.generateTrees(n)):
    inorder_print(i)
    print("and")


