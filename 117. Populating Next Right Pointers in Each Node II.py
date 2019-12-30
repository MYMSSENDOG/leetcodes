from bNode_lib import *
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        q = [root]
        while q:
            for i in range(len(q) - 1):
                if i != len(q) - 1:
                    q[i].next = q[i + 1]
            q[-1].next = None

            for i in range(len(q)):
                t = q.pop(0)
                if t.left:
                    q.append(t.left)
                if t.right:
                    q.append(t.right)

        return root

sol = Solution()
p = makeTree([1,2,3,4,5,6,7])
inorder_next_print(sol.connect(p))