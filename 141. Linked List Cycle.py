# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from node_lib import *
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head.next == head:
            return True
        c1 = 0
        cur = head

        while cur:
            cur = cur.next
            c1 += 1
            cur2 = head
            for i in range(c1):
                cur2 = cur2.next
                if i+1 != c1  and cur2 == cur:
                    return True
        return False
sol = Solution()
head = makeNode([1])
cur = head
pos = 1
i = 0
temp = None
while cur.next != None:
    i +=1
    cur = cur.next
    if i == pos:
        temp = cur
cur.next = temp
print(sol.hasCycle(head))