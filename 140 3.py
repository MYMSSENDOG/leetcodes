class Solution:
    def wordBreak(self, s, wordDict):
        memo = {"":[""]}
        def helper(s):
            if s in memo:
                return memo[s]
            ret = []
            for w in wordDict:
                if s.endswith(w):
                    ret+=[(pre and pre + " "  )+ w for pre in helper(s[:-len(w)]) ]

            memo[s] = ret
            return memo[s]
        return helper(s)

sol = Solution()
s = "aaaaaaaaaaaaaaaa"

wordDict = ["a","aaa","aa","aaaa","aaaaa"]
print(sol.wordBreak(s,wordDict))