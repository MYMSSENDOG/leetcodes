class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

def inorder_print(head, arr):
    if head.left:
        inorder_print(head.left,arr)
    arr.append(head.val)
    if head.right:
        inorder_print(head.right, arr)
def postorder_print(head,arr):
    if head.left:
        postorder_print(head.left, arr)
    if head.right:
        postorder_print(head.right, arr)
    arr.append(head.val)

def makeArray(root):
    ret = []
    if not root:
        return []
    cur = root
    q = [cur]
    while q:
        t = q.pop(0)
        ret.append(t.val)
        if t.left:
            pass



def makeTree(array):
    n = len(array)
    if n == 0:
        return None
    tree_list = [TreeNode(0) for i in range(len(array))]
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


def MorrisTraversal(root,val_list):
    # Set current to root of binary tree
    current = root

    while (current is not None):

        if current.left is None:
            #print(current.val)
            val_list.append(current.val)
            current = current.right
        else:
            # Find the inorder predecessor of current
            pre = current.left
            while (pre.right is not None and pre.right != current):
                pre = pre.right

                # Make current as right child of its inorder predecessor
            if (pre.right is None):
                pre.right = current
                current = current.left

                # Revert the changes made in if part to restore the
            # original tree i.e., fix the right child of predecessor
            else:
                pre.right = None
                #print (current.val)
                val_list.append(current.val)
                current = current.right
#inorder_print(makeTree([1,2,3,None,None,4,5]))
