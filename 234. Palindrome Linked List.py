# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from node_lib import *

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        n = 0
        cur = head
        while cur:
            n +=1
            cur = cur.next
        if n == 1:
            return True
        if n == 2:
            return head.val == head.next.val
        cur = head
        end = None
        start = None
        for i in range((n+1)//2):
            cur = cur.next
        for i in range(n//2):
            t = cur.next
            start = cur
            start.next = end
            end = start
            cur = t
        for i in range(n//2):
            if start.val != head. val:
                return False
            start = start.next
            head = head.next
        return True
sol = Solution()
head= makeNode([1,1,2,1])
print(sol.isPalindrome(head))