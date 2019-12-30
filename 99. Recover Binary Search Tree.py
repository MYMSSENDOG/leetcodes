from tree_node_lib import *
import sys
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        first = None
        second = None
        pre = TreeNode(-sys.maxsize-2)
        print(pre.val)
        ret = root
        while root:
            if not root.left:
                if pre.val > root.val:
                    second = root
                    if not first:
                        first = pre
                pre = root
                root = root.right
            else:
                temp = root.left
                while temp.right !=None and temp.right != root:
                    temp = temp.right
                if temp.right:
                    if pre.val>root.val:
                        second = root
                        if not first:
                            first = pre
                    pre = root
                    temp. right = None
                    root = root.right
                else:
                    temp.right = root
                    root = root.left

        first.val, second.val = second.val,first.val
        inorder_print(ret)

sol = Solution()
n = makeTree([1,3,None,None,2])
sol.recoverTree(n)