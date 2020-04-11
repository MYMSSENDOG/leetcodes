import collections
class Solution:
    def firstUniqChar(self, s: str) -> int:
        n = len(s)
        d = collections.defaultdict(int)
        for c in s:
            d[c] +=1
        for i, c in enumerate(s):
            if d[c] == 1:
                return i
        return -1


sol = Solution()
s = "leetcode"
print(sol.firstUniqChar(s))