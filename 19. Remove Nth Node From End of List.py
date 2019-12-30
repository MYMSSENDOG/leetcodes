def pr(node):
    while node != None:
        print (node.val)
        node = node.next

def makeNode(n):
    head = ListNode(1)
    cur = head
    for i in range (2, n+1):
        cur.next = ListNode(i)
        cur = cur.next
    return head

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None




class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        cur_node = head
        nodes = []

        while cur_node != None:
            nodes.append(cur_node)
            cur_node = cur_node.next
        if n == len(nodes):
            if (n == 1):
                return None
            else:
                return nodes[1]

        else:
            if n == 1:
                nodes[-2].next = None
            else:
                nodes[-n - 1].next = nodes[-n + 1]

        return head

head = makeNode(2)
cur_node = head
n = 1
solver = Solution()
pr(solver.removeNthFromEnd(head,n))
