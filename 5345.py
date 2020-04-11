class Solution:
    def validateBinaryTreeNodes(self, n: int,leftChild, rightChild) -> bool:
        root = 0
        q = [root]
        i = 0
        d = {}
        d[root] = 1
        while i < n:
            for k in range(len(q)):
                t = q.pop()
                l =  leftChild[i]
                r = rightChild[i]
                if l != -1:
                    if l not in d:
                        d[l] = 1
                        q.append(l)
                    else:
                        return False
                if r != -1:
                    if r not in d:
                        d[r] = 1
                        q.append(r)
                    else:
                        return False
                i +=1
            if not len(q) and i < n:
                return False
        return True





n = 6
leftChild =[1,-1,-1,4,-1,-1]
rightChild = [2,-1,-1,5,-1,-1]
sol = Solution()
print(sol.validateBinaryTreeNodes(n, leftChild, rightChild))


"""


a b c d e ...
2*sum - i

"""