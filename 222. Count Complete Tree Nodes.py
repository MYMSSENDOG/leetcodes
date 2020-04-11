from tree_node_lib import *

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        level = 0
        cur = root
        l = cur
        r = cur
        while 1:
            l = l.left
            r = r.right
            if l and r :
                level += 1
                continue
            elif not l and not r:
                return 2**(level+1)-1
            else:
                break

        l = 0
        r = 2**(level + 1) - 1

        while l<r:
            m = (l + r) //2
            cur = root
            # binary search 하자 level 만큼 비트 필요
            for b in reversed(range(level+1)):
                if m & (2**b):
                    cur = cur.right
                else:
                    cur = cur.left
            if cur:
                l = m + 1
            else:
                r = m
        m = (l + r) //2
        return 2 ** (level+1) + m-1


sol = Solution()
root = makeTree([1,2])
print(sol.countNodes(root))