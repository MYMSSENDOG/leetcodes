class Solution:
    def maximalSquare(self, matrix) -> int:
        m = len(matrix)
        if not m or not matrix[0]:
            return 0
        n = len(matrix[0])
        M = 0
        h = [0] * n
        l = [0] * n
        r = [n] * n
        for i in range(m):
            cur_left = 0
            cur_right = n
            for j in range(n):
                if matrix[i][j] == "1":
                    h[j] +=1

                    l[j] = max(cur_left, l[j])
                else:
                    h[j] = 0

                    cur_left = j+1
                    l[j] = 0
            for j in reversed(range(n)):
                if matrix[i][j] == "1":
                    r[j] = min(r[j], cur_right)
                else:
                    cur_right = j
                    r[j] = n
            for j in range(n):
                M = max(M, min( h[j],-l[j] + r[j] )**2)
        return M
matrix = ["10101","11111","11111","11111","11111","11111"]

sol = Solution()
print(sol.maximalSquare(matrix))