# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
class BinaryMatrix:
    def __init__(self, mat):
        self.mat = mat
    def get(self, x: int, y: int) -> int:
        return self.mat[x][y]
    def dimensions(self):
        return [len(self.mat), len(self.mat[0])]

class Solution:
    def leftMostColumnWithOne(self, mat) -> int:
        B = BinaryMatrix(mat)
        binaryMatrix = B
        m, n = binaryMatrix.dimensions()
        cand = set([i for i in range(m)])

        l = 0
        r = n

        while l < r:
            mid = (l + r) // 2
            to_del = set()
            for row in cand:
                cur = binaryMatrix.get(row,mid)
                if not cur:
                    to_del.add(row)
                else:
                    break
            else:
                l = mid+1
                continue

            r = mid
            cand -= to_del
        if l == n:
            return -1
        return l


sol = Solution()
mat = [[0,0],[0,0]]
print(sol.leftMostColumnWithOne(mat))
