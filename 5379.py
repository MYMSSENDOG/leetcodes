class Solution:
    def stoneGameIII(self, stoneValue) -> str:
        n = len(stoneValue)
        dp = [0] * n
        dp[-1] = stoneValue[-1]
        for i in range(n-2,-1,-1):
            r = -99999999
            for j in range(3):
                if i+j < n:
                    t = sum(stoneValue[i:i+j+1])
                    if i+j+1 >= n:
                        sub = 0
                    else:
                        sub = dp[i+j+1]
                    r = max(r, t - sub)
            dp[i] = r
        if dp[0] > 0:
            return "Alice"
        if dp[0] == 0:
            return "Tie"
        if dp[0] < 0:
            return "Bob"

sol = Solution()
values = [1,2,3,6]
print(sol.stoneGameIII(values))