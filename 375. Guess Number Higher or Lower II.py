class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp=[[0] * (n+2) for _ in range(n+2)]

        for i in range(n,0,-1):
            for j in range(i+1,n+1):
                dp[i][j] = min(x + max(dp[i][x-1], dp[x+1][j]) for x in range(i,j+1))
        return dp[1][n]

sol = Solution()
n = 20
print(sol.getMoneyAmount(n))