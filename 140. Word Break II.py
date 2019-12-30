class Solution:
    def wordBreak(self, s: str, wordDict) :
        dict = {}
        m = 9999
        M = 0
        ret = []
        for i in range(len(wordDict)):
            dict[wordDict[i]] = i
            M = max(M,len(wordDict[i]))
            m = min(m,len(wordDict[i]))
        dp = [[]for i in range(len(s) + 1)]

        dp[-1] =[[]]


        for i in range(len(dp)):#dp[i] means that if s[0] ~ s[i] can be segmented by word in  wordDict
            for j in range(m,M+1):
                if i - j < -1:
                    break
                dp[i] = [x + " " + s[i+1-j:i+1] for x in dp[i-j] for j in range(m,M+1)]


        index = dp[len(s) - 1]
        for i in index:
            t = wordDict[i[0]]
            for j in i[1:]:
                t += " " + wordDict[j]
            ret.append(t)
        return ret

sol = Solution()
s = "aaa"

wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
print(sol.wordBreak(s,wordDict))