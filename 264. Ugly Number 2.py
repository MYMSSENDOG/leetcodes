import sys
import math
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1] * n
        t2, t3, t5 = 0,0,0

        for i in range(1,n):
            dp[i] = min(dp[t2] * 2, dp[t3] * 3, dp[t5] * 5)
            if dp[i] == dp[t2] * 2:
                t2 +=1
            if dp[i] == dp[t3] * 3:
                t3 +=1
            if dp[i] == dp[t5] * 5:
                t5 +=1
        return dp[-1]

sol = Solution()
n = 83
print(sol.nthUglyNumber(n))