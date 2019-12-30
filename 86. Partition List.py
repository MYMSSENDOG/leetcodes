from node_lib import *

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        n = get_size(head)
        small = None
        small_cur = None
        big = None
        big_cur = None
        cur = head

        for i in range(n):
            if cur.val < x:
                if not small:
                    small = cur
                    small_cur = cur
                else:
                    small_cur.next = cur
                    small_cur = small_cur.next
            else:
                if not big:
                    big = cur
                    big_cur = cur
                else:
                    big_cur.next = cur
                    big_cur = big_cur.next
            cur = cur.next
        if big_cur:
            big_cur.next = None
        if small:
            small_cur.next = big
            return small
        else:
            return big

n = makeNode([1,4,3,2,5,2])
x = 3
sol = Solution()
pr(sol.partition(n, x))