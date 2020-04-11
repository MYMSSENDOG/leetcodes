
from tree_node_lib import *
class Codec:
    def serialize(self, root):
        if not root:
            return None
        q = [root]
        ret = []
        while q:
            for i in range(len(q)):
                t = q.pop(0)
                if t != None:
                    ret.append(t.val)
                    q.append(t.left)
                    q.append(t.right)
                else:
                    ret.append(None)
        for i in reversed(range(len(ret))):
            if ret[i] != None:
                return ret[:i+1]


    def deserialize(self, data):
        if not data:
            return None
        q = [TreeNode(data[0])]
        ret = q[0]
        i = 1
        while i < len(data):
            t = q.pop(0)
            if data[i] != None:
                t.left = TreeNode(data[i])
                q.append(t.left)
            i+=1
            if i < len(data):
                if data[i] != None:
                    t.right = TreeNode(data[i])
                    q.append(t.right)
                i+=1
            else:
                break
        return ret
codec = Codec()
inorder_print(codec.deserialize([1,2,3,4,5,None,None,6,7]))
a = makeTree([1,2,3,4,None])
print(codec.serialize(a))
