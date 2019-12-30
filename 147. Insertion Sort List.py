# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from node_lib import *
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        def sort(array, n):
            if not array:
                array.append(n)
                return
            l = 0
            r = len(array) - 1
            while r>l + 1:
                m = (l + r)//2
                if array[m][0] < n[0]:
                    l = m
                elif array[m][0] > n[0]:
                    r = m
                elif array[m][0] == n[0]:
                    l = m
                    r = m
                    break
            if array[l][0] > n[0]:
                array.insert(l,n)
            elif array[r][0] < n[0]:
                array.insert(r+1, n)
            else:
                array.insert(r, n)
        ret = []
        cur = head
        while cur:
            t = [cur.val, cur]
            sort(ret,t)
            cur = cur.next
        for i in range(len(ret)-1):
             ret[i][1].next = ret[i+1][1]
        ret[-1][1].next= None
        return ret[0][1]


sol = Solution()
node = makeNode(([4,2,1,3,5,7,9,8]))
pr(sol.insertionSortList(node))
