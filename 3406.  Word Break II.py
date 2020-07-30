class Solution:
    def wordBreak(self, s: str, wordDict):
        minl = 999
        maxl = 0
        memo = {}

        def helper(start):
            ret = []
            if start in memo:
                return memo[start]
            if start >= len(s):
                return [""]

            for i in range(minl, maxl + 1):
                if start + i > len(s):
                    break
                if s[start:start + i] in wordDict:
                    ret += [s[start:start + i] +" " + post for post in  helper(start + i)]
            memo[start] = ret
            return ret
        for w in wordDict:
            minl = min(len(w), minl)
            maxl = max(maxl, len(w))
        ret =  helper(0)
        for i in range(len(ret)):
            ret[i] = ret[i].rstrip()
        return ret










sol = Solution()
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
print(sol.wordBreak(s, wordDict))