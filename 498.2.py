class Solution:
    def findDiagonalOrder(self, matrix):
        ret = []
        m = len(matrix)
        if not m:
            return []
        n = len(matrix[0])
        d = m + n - 1
        for i in range(d):
            start = (min(i, m - 1))
            end = max(0, i - (n - 1))
            for j in range(end, start+1)[::i%2 * 2 - 1]:
                ret.append(matrix[j][i-j])
        return ret



sol = Solution()
matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

print(sol.findDiagonalOrder(matrix))
