class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        #dp[s][t]는 s[s] 까지 t[t]가 몇 개 포함 되어 있나
        m = len(s)
        n = len(t)
        if m<n:
            return 0
        dp = [[0] * n for i in range(m)]
        if s[0] == t[0]:
            dp[0][0] = 1
            for i in range(1, n):
                if s[i] == t[i]:
                    dp[i][i] = 1
                else:
                    break
        for i in range(1,m):
            dp[i][0] = dp[i-1][0] + 1 if s[i] == t[0] else dp[i-1][0]
        for i in range(1,n):
            for j in range(i+1,m):
                if s[j] != t[i]:
                    dp[j][i] = dp[j-1][i]
                else:
                    dp[j][i] = dp[j-1][i] + dp[j-1][i-1]
        return dp[-1][-1]





sol = Solution()

S = "aacaacca"
T = "ca"
print(sol.numDistinct(S,T))