from node_lib import *

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        n = get_size(head)
        k = k%n
        cur_node = head
        step = 0
        if not k:
            return head
        while cur_node.next!=None:
            if step == n -k-1:
                tp = cur_node
            cur_node =cur_node.next
            step += 1
        cur_node.next = head
        ret = tp.next
        tp.next = None
        return ret
sol = Solution()
nodes = makeNode([1,2,3,4,5])
k = 0
s = sol.rotateRight(nodes,k)
pr(s)