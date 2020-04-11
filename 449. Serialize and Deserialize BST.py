# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from tree_node_lib import *
class Codec:

    def serialize(self, root: TreeNode) -> str:
        ret = ""
        if not root:
            return ret
        q = [root]
        while q:
            for i in range(len(q)):
                t = q.pop(0)
                if t == None:
                    ret += "None"
                    continue
                ret+=t.val
                q.append(t.left)
                q.append(t.right)
        return ret
    def deserialize(self, data: str) -> TreeNode:
        if not data:
            return None
        head = TreeNode(data[0])
        q = [head]
        i = 1
        while q:
            for _ in range(len(q)):
                t = q.pop(0)
                if t == None:# " . 이든 None 이든 바꾸기ㅏ
                    continue
                if i<len(data):
                    t.left = TreeNode(data[i])
                    q.append(t.left)
                    i+=1
                if i < len(data):
                    t.right = TreeNode(data[i])
                    q.append(t.right)
                    i+=1
                else:
                    return head


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))