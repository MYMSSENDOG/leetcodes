
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        ret = []
        if not head:
            return None

        q = [head]
        while q:
            t = q.pop()
            ret.append(t.val)
            if t.next:
                q.append(t.next)
            if t.child:
                q.append(t.child)
        head = Node(ret[0], None, None, None)
        prev = head
        for i, e in enumerate(ret[1:], 1):
            n = Node(e, prev, None, None)
            prev.next = n
            prev = n
        return head
sol = Solution()
head = [1,2,3,4,5,6,None,None,None,7,8,9,10,None,None,11,12]
print(sol.flatten(head))
