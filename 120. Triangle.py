class Solution:
    def minimumTotal(self, triangle) -> int:
        m = len(triangle)

        if not triangle or not triangle[0]:
            return 0
        dp = [0] * m
        dp[0] = triangle[0][0]
        for i in range(1,m):
            t1 = dp[0]
            dp[0] = triangle[i][0] + t1
            for j in range(1,i):
                t2 = dp[j]
                dp[j] = min(t1, dp[j]) + triangle[i][j]
                t1= t2
            dp[i]= t1 + triangle[i][i]
        return min(dp)
t = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
sol = Solution()
print(sol.minimumTotal(t))