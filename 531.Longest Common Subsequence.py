class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [0] * (m+1)

        for r in range(n):
            prev = 0
            for l in range(m):
                if text2[r] == text1[l]:
                    temp = dp[l]
                    dp[l] = prev + 1
                    prev = temp
                else:
                    prev = dp[l]
                    dp[l] = max(dp[l], dp[l-1])
        return dp[-2]
sol = Solution()
text1 = "bsbininm"
text2 = "jmjkbkjkv"
print(sol.longestCommonSubsequence(text1, text2))