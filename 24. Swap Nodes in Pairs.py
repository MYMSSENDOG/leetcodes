from node_lib import *


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        node_list = []
        if head == None:
            return None
        node = head
        while node != None:
            node_list.append(node)
            node = node.next
        n = len(node_list)
        i = 0
        while n - 2 >= 0:
            node_list[i], node_list[i+1] =node_list[i+1], node_list[i]
            i+=2
            n -= 2
        node_list[i+n-1].next = None
        node_list_to_nodes(node_list)
        return node_list[0]

sol = Solution()
l1 = makeNode([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
ret = sol.swapPairs(l1)
pr(ret)
