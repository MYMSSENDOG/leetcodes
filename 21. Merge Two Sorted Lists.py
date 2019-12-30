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
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        nodes = []

        c1 = l1
        c2 = l2
        while c1 != None and c2 != None:
            if c1.val < c2.val:
                nodes.append(c1)
                c1 = c1.next
            else:
                nodes.append(c2)
                c2 = c2.next

        if c1 == None:
            if c2 == None:
                return None
            while c2 != None:
                nodes.append(c2)
                c2 = c2.next
        elif c2 == None:
            while c1 != None:
                nodes.append(c1)
                c1 = c1.next
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        return nodes[0]
s = Solution()
l1 = makeNode(5)
l2 = makeNode(4)
pr(s.mergeTwoLists(l1,l2))