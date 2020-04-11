# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import copy
from tree_node_lib import *
from node_lib import *

class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        d = {}
        q = [[root, str(root.val)]]
        d[str(root.val)] = 1
        n = 1
        cur_node = head
        s = str(head.val)
        while cur_node.next:
            cur_node = cur_node.next
            n +=1
            s+= str(cur_node.val)
        while q:
            for i in range(len(q)):
                t, v = q.pop(0)
                v += str(t.val)
                d[str(t.val)] = 1
                if len(v) == n:
                    d[v] = 1
                    v = v[1:]
                if t.left:
                    q.append([t.left, v])
                if t.right:
                    q.append([t.right, v])

        return s in d

sol = Solution()
head = makeNode([1,10])
root = makeTree([1,4,4,None,2,2,None,1,None,6,8,None,None,None,None,1,3])

print(sol.isSubPath(head,root))