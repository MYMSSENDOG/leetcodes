
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children



class Solution:
    def levelOrder(self, root: Node):
        cur = root
        ret = []
        if not root:
            return []
        q = [cur]
        while q:
            this_level = []
            for i in range(len(q)):
                t = q.pop(0)
                this_level.append(t.val)
                for c in t.children:
                    q.append(c)
            ret.append(this_level)
        return ret

sol = Solution()
root = [1,None,2,3,4,5,None,None,6,7,None,8,None,9,10,None,None,11,None,12,None,13,None,None,14]
print(sol.levelOrder(root))