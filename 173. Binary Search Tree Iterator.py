
from tree_node_lib import *
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root = root
        self.q = []


    def next(self) -> int:
        return self.q.pop(0)

    def hasNext(self) -> bool:
        return not not self.q
    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        self.q.append(root.val)
        self.inorder(root.right)

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()