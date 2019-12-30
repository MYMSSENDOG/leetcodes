from node_lib import *

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        node_list = []
        if head == None:
            return None
        node = head
        while node != None:
            node_list.append(node)
            node = node.next
        n = len(node_list)
        i = 0
        while i + k<=n:
            temp = node_list[i:i+k]
            temp.reverse()
            node_list[i:i + k] = temp
            i += k
        if i != n:
            temp  = node_list[i:n]
            temp.reverse()
            node_list[i:n] = temp
        node_list[n - 1].next = None
        node_list_to_nodes(node_list)
        return node_list[0]
sol = Solution()
l1 = makeNode([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
k = 5
ret = sol.reverseKGroup(l1, k)
pr(ret)