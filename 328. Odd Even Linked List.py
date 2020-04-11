# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from node_lib import *
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:

        cur = head
        odd_tail = None
        even_start = None
        even_tail = None
        i = 1
        while cur:
            if i %2 == 1:
                if not odd_tail:
                    odd_tail = cur
                else:
                    odd_tail.next = cur
                    odd_tail = odd_tail.next


            else:
                if not even_start:
                    even_start = cur
                    even_tail = cur
                else:
                    even_tail.next = cur
                    even_tail = even_tail.next
            t = cur
            cur = cur.next
            t.next = None
            i+=1
        odd_tail.next = even_start
        return head

sol = Solution()
head= makeNode([1,2,3,4,5,None])
pr(sol.oddEvenList(head))
