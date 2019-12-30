class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def makeTree(array):
    n = len(array)
    if n == 0:
        return None
    tree_list = [Node(0,None,None,None) for i in range(len(array))]
    tree_list[0].val = array[0]
    parent = [0]
    i = 1
    num_of_parent = 1

    children_would_be_parent = []
    while i < n:
        for j in parent:
            if i < n:
                if array[i] == None:
                    tree_list[j].left = None
                else:
                    tree_list[i].val = array[i]
                    tree_list[j].left =tree_list[i]
                    children_would_be_parent.append(i)
                i +=1
            if i < n:
                if array[i] == None:
                    tree_list[j].right = None
                else:
                    tree_list[i].val = array[i]
                    tree_list[j].right =tree_list[i]
                    children_would_be_parent.append(i)
                i +=1
            else:
                break
        parent = children_would_be_parent
        children_would_be_parent = []
    return tree_list[0]

def inorder_next_print(root:Node):
    if not root:
        return
    inorder_next_print(root.left)
    print(root.val)
    if root.next:
        print("next is ", root.next.val)
    inorder_next_print(root.right)