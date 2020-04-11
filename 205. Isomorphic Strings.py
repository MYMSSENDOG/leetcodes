import collections
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = collections.defaultdict(str)
        o = collections.defaultdict(int)
        for i in range(len(s)):
            if not d[s[i]]:
                if not o[t[i]]:
                    o[t[i]] = 1
                    d[s[i]] = t[i]
                else:
                    return False
            elif d[s[i]] == t[i]:
                continue
            else:
                return False
        return True

sol = Solution()
s1 = "ab"
s2 = "aa"
print(sol.isIsomorphic(s1,s2))

