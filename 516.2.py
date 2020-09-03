class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[1] * n for _ in range(n)]
        for length in range(1,n):# 길이
            for l in range(0, n-length):#왼쪽
                r = l + length
                if s[l] == s[r]:
                    if l + 1 == r:
                        dp[l][r] = 2
                    else:
                        dp[l][r] = dp[l+1][r-1]+2
                else:
                    dp[l][r] = max(dp[l+1][r],dp[l][r-1])
        return dp[0][-1]





sol = Solution()
s = "aaaba"
print(sol.longestPalindromeSubseq(s))