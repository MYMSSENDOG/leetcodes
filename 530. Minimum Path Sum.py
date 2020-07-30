class Solution:
    def minPathSum(self, grid) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [0] * n
        dp[0] = grid[0][0]
        for i in range(1,n):
            dp[i] = dp[i-1] + grid[0][i]
        for y in range(1,m):
            for x in range(n):
                if x > 0:
                    dp[x] = min(dp[x - 1], dp[x]) + grid[y][x]
                else:
                    dp[x] = dp[x] + grid[y][x]
        return dp[-1]




grid =[
    [1,3,1],
    [1,5,1],
    [4,2,1]
]
sol = Solution()
print(sol.minPathSum(grid))