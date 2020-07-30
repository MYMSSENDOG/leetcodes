# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from node_lib import *
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        odd_tail = head
        even_head = head.next
        even_tail = even_head
        cur = even_head.next
        i = 1
        while cur:
            if i %2 == 1:
                odd_tail.next = cur
                odd_tail = cur
            else:
                even_tail.next = cur
                even_tail = cur
            cur = cur.next
            i+=1
        even_tail.next = None
        odd_tail.next = even_head
        return head
sol = Solution()
head = makeNode([1,2,3,4,5])
pr(sol.oddEvenList(head))