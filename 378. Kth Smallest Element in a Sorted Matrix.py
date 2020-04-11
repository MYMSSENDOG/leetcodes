import bisect
class Solution:
    def kthSmallest(self, matrix, k: int) -> int:

        m = len(matrix)
        if not matrix:
            return None
        n = len(matrix[0])
        q = [[matrix[0][0], 0, 0]]
        d = [m] * n
        d[0] = 0

        for i in range(k-1):

            v, y, x = q.pop(0)
            if y+1<m:
                bisect.insort_left(q, [matrix[y+1][x], y+1, x])
            if x + 1< n and d[x+1] > y:
                d[x+1] = y
                bisect.insort_left(q, [matrix[y ][x+1], y, x+1])
        return q.pop(0)[0]





sol = Solution()
matrix = [
             [1, 5, 9],
             [10, 11, 13],
             [12, 13, 15]
         ]
k = 8
print(sol.kthSmallest(matrix, k))