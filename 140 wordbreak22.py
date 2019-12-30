class Solution:
    def wordBreak(self, s, wordDict):
        memo = {}

        if 1:#내가쓴거 할땐 입력 aaaaaaaaaaaaaaaa + B
            memo = {-1: [""]}
            for i in range(len(s)):
                for j in range(0,i+1):
                    for pre in memo[j-1]:
                        if s[j:i+1] in wordDict:
                            memo[j-1] += [pre + " "  + s[j:i+1]]

            return memo[len(s) - 1]

        else:#다른사람거 할땐 입력 B + aaaaaaaaaaaaaaaaaaaa
            memo = {len(s): ['']}
            def sentences(i):
                if i not in memo:
                    memo[i] = [s[i:j] + (tail and ' ' + tail)
                               for j in range(i+1, len(s)+1)
                               if s[i:j] in wordDict
                               for tail in sentences(j)]
                return memo[i]
            return sentences(0)
sol = Solution()
s = "aaaaaaa"

wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa"]
print(sol.wordBreak(s,wordDict))