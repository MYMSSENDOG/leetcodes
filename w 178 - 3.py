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

        q = [root]
        while q:
            for _ in range(len(q)):
                t = q.pop(0)
                if t.left:
                    q.append(t.left)
                if t.right:
                    q.append(t.right)

                #만약 헤드랑 같으면 검사시작
                if t.val == head.val:
                    cur_node = head
                    cur_node = cur_node.next
                    if not cur_node:
                        return True
                    qq = copy.deepcopy((q))
                    while cur_node:
                        here = False
                        for i in range(len(qq)):
                            k = qq.pop(0)

                            if k.val == cur_node.val:
                                here = True
                                if k.left:
                                    qq.append(k.left)
                                if k.right:
                                    qq.append(k.right)

                        if not cur_node.next and here:
                            return True
                        else:
                            cur_node = cur_node.next
                        if not qq:
                            break

        return False

sol = Solution()
head = makeNode([1,4,2,1])
root = makeTree([1,4,4,None,2,2,None,1,None,6,8,None,None,None,None,1,3])

print(sol.isSubPath(head,root))