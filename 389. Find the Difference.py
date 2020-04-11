import collections
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d = collections.defaultdict(int)
        for i in range(len(s)):
            d[s[i]] +=1
        for i in range(len(t)):
            d[t[i]] -=1
            if d[t[i]] == -1:
                return t[i]


sol = Solution()
s = "abcd"
t = "abced"
print(sol.findTheDifference(s,t))