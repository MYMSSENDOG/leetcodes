from bNode_lib import *
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        head = Node(None,None,None,None)
        prev = Node(None,None,None,None)
        prev = None
        head = None
        cur = root
        while cur:
            if cur.left:
                if not prev:
                    head = cur.left
                else:
                    prev.next = cur.left
                prev = cur.left
            if cur.right:
                if not prev:
                    head = cur.right
                else:
                    prev.next = cur.right
                prev = cur.left
            cur = cur.next
            if cur == None:
                cur = head
                head = None
                prev = None
        return root
sol = Solution()
p = makeTree([1,2,None,4,5])
inorder_next_print(sol.connect(p))