def pr(node):#전체 프린트
    temp = node
    while temp != None:
        print (temp.val)
        temp = temp.next

def get_size(node):
    n = 0
    while node!= None:
        node = node.next
        n += 1
    return n

def makeNode(n):
    if len(n) == 0:
        return None
    head = ListNode(n[0])
    cur = head
    for i in range (1, len(n)):
        cur.next = ListNode(n[i])
        cur = cur.next
    return head

def node_list_to_nodes(ret):
    for i in range(len(ret) - 1):
        ret[i].next = ret[i+1]
    return ret

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None