class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n+1)
        dp[1] = 0 if s[0] =="0" else 1
        dp[0] = 1
        for i in range(2,n+1):
            if s[i-1]!="0":
                dp[i] += dp[i-1]
            a = int(s[i-2]) * 10 + int(s[i-1])
            if a >=10 and a<=26:
                dp[i] += dp[i-2]
        return dp[n]



sol  = Solution()
i = "10"
print(sol.numDecodings(i))