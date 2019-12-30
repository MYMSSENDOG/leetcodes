class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)
        if n1<n2:
            n1 ,n2 = n2, n1
            word1 , word2 = word2, word1
        dp = [0]* (n2+1)
        for i in range(1,n2+1):
            dp[i] = i
        for i in range(1,n1+1):
            p = dp[0]
            dp[0] = i
            for j in range(1,n2+1):
                temp = dp[j]
                if word1[i-1] == word2[j-1]:
                    dp[j] = p
                else:
                    dp[j] = min(p,dp[j],dp[j-1])+1
                p = temp
        return dp[n2]




word1 = "intention"
word2 = "execution"


sol = Solution()
print(sol.minDistance(word1,word2))
