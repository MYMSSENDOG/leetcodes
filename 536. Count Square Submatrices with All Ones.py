class Solution:
    def countSquares(self, matrix) -> int:
        m = len(matrix)
        n = len(matrix[0])
        ret = 0
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            cur = 0
            for j in range(n):
                if matrix[i][j] == 1:
                    cur +=1
                if i == 0:
                    dp[i][j] = cur
                else:
                    dp[i][j] = cur + dp[i-1][j]

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    continue
                side = 0
                while i - side >= 0 and j - side >= 0:
                    a = i- side
                    b = j - side
                    if dp[i][j] - dp[a - 1][j] - dp[i][b-1] + dp[a-1][b-1] == (side+1)**2:
                        ret +=1
                        side +=1
                    else:
                        break
        return ret
matrix =[[0,1,1,1],
         [1,1,1,1],
         [0,1,1,1]]
sol = Solution()
print(sol.countSquares(matrix))