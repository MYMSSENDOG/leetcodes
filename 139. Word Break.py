class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        dict = {}
        m = 9999
        M = 0

        for i in wordDict:
            dict[i] = 1
            M = max(M,len(i))
            m = min(m,len(i))
        dp = [False] * (len(s) + M)
        for i in range(-M,0):
            dp[i] = True
        for i in range(len(dp)):#dp[i] means that if s[0] ~ s[i] can be segmented by word in  wordDict
            for j in range(m,M+1):
                if (dp[i-j]and s[i+1-j:i+1] in dict):
                    dp[i] = True
                    break
        return dp[len(s) - 1]





sol = Solution()
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
print(sol.wordBreak(s, wordDict))
s ="leetcode"
wordDict = ["leet", "code"]
print(sol.wordBreak(s, wordDict))
