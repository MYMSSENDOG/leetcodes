import collections
class Solution:
    def findAnagrams(self, s: str, p: str):
        d = collections.defaultdict(int)
        d2 = collections.defaultdict(int)
        if len(s) < len(p):
            return []
        ret = []
        for c in p:
            d[c] += 1
        k = len(p)
        for i in range(k - 1):
            d2[s[i]] += 1
        for r in range(k-1, len(s)):
            l = r - k + 1
            d2[s[r]] += 1
            for c in d:
                if d[c] == d2[c]:
                    continue
                break
            else:
                ret.append(l)
            d2[s[l]] -=1
        return ret


s= "aaa"
p= "aa"
sol = Solution()
print(sol.findAnagrams(s,p))