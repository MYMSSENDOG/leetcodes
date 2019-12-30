# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from node_lib import *

class Solution:
    def sortList(self, head: ListNode) -> ListNode:

        def merge(n1, n2):
            ret = n1
            while n1.next:
                n1 = n1.next
            n1.next = n2
            return ret
        def quick(node):
            if not node or not node.next:
                return node
            pivot = node
            pivot_tail = node
            cur = node.next
            l_start = None
            l_end = None
            r_start = None
            r_end = None
            ret = None
            while cur:
                if cur.val < pivot.val:
                    if not l_start:
                        l_start = cur
                        l_end = cur
                    else:
                        l_end.next = cur
                        l_end = cur

                elif cur.val > pivot.val:
                    if not r_start:
                        r_start = cur
                        r_end = cur
                    else:
                        r_end.next = cur
                        r_end = cur
                else:
                    pivot_tail.next = cur
                    pivot_tail = cur
                cur = cur.next
            pivot_tail.next = None
            ret = pivot
            if r_end:
                r_end.next = None
                r_node = quick(r_start)
                ret = merge(pivot,r_node)
            if l_end:
                l_end.next = None
                l_node = quick(l_start)
                ret = merge(l_node,pivot)
            return ret
        return quick(head)

sol = Solution()
n = makeNode([1,1,1,2,2,2,1,1])

pr(sol.sortList(n))