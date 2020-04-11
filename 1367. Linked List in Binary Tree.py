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
from tree_node_lib import *
from node_lib import *

class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        list_node = []
        cur_node = head
        while cur_node:
            list_node.append(cur_node.val)
            cur_node = cur_node.next
        q = [[root,[0]]]
        while q:
            for _ in range(len(q)):
                t, indexes = q.pop(0)
                if not t:
                    continue
                next_indexes = [0]
                for i in indexes:
                    if t.val == list_node[i]:
                        next_indexes.append(i+1)
                        if i +1 == len(list_node):
                            return True
                q.append([t.left, next_indexes])
                q.append([t.right, next_indexes])
        return False

sol = Solution()
head = makeNode([3])
root = makeTree([1,4,4,None,2,2,None,1,None,6,8,None,None,None,None,1,3])

print(sol.isSubPath(head,root))