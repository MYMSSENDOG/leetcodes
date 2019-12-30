# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from node_lib import *
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next :
            return head
        cur = head
        cur_val = cur.val
        start = None
        tail = None
        stack = 1
        pre = cur
        cur = cur.next
        while cur != None:
            if cur_val == cur.val:
                stack+=1
            else:
                if stack>1:
                    #이전거 완전히 버려도 됨
                    pass
                elif stack == 1:
                    #이전거 테일에 붙여야됨
                    if not start:
                        start = pre
                        tail = pre
                        tail.next = None
                    else:
                        tail.next = pre
                        tail = pre
                stack = 1
                cur_val = cur.val
            pre = cur
            cur = cur.next
        if stack == 1:
            if not start:
                start = pre
                tail = pre
            else:
                tail.next = pre
                tail = pre
        if not tail:
            return None
        tail.next = None
        pr(start)

sol = Solution()
n = makeNode([1,1,2])
print(sol.deleteDuplicates(n))