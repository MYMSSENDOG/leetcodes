# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from tree_node_lib import *
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        def helper(root):
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                temp = root
                cur_p = root
                cur = root.left
                while cur.right:
                    cur_p = cur
                    cur = cur.right
                if cur.val == temp.left.val:
                    cur.right = temp.right
                    return cur
                else:
                    cur_p.right = cur.left
                    cur.right = temp.right
                    cur.left = temp.left
                    return cur

        if not root:
            return None
        q = [[root, None]]
        found = False
        to_del = None
        parent_del = False
        while q:
            if not found:
                for i in range(len(q)):
                    t, p = q.pop(0)
                    if t.val == key:
                        to_del = t
                        parent_del = p
                        found = True
                        break
                    else:
                        if t.left:
                            q.append([t.left, t])
                        if t.right:
                            q.append([t.right, t])
            else:
                break
        if not found:
            return root
        if not parent_del:
            return helper(root)
        if parent_del.left and parent_del.left.val == key:
            parent_del.left = helper(to_del)
        else:
            parent_del.right = helper(to_del)
        return root




                #왼쪽에서 가장 큰 값 찾기




sol = Solution()
root = makeTree([5,3,6,2,4,None,7])
key = 5
inorder_print(sol.deleteNode(root, key))
