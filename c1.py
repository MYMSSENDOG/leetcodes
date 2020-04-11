class Solution:
    def kWeakestRows(self, mat, k: int):
        q = []
        for i, e in enumerate(mat):
            q.append([e.count(1), i])
        q.sort()
        ret = []
        for i in range(k):
            ret.append(q[i][1])
        return ret

sol = Solution()
mat = \
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]],
k = 3
print(sol.kWeakestRows(mat,k))