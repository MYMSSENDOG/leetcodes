import collections
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1 = collections.defaultdict(int)
        d2 = collections.defaultdict(int)
        if len(s1) > len(s2):
            return False
        for c in s1:
            d1[c] +=1
        for i in range(len(s1) - 1):
            d2[s2[i]] +=1

        for i in range(len(s1)-1, len(s2)):
            d2[s2[i]] += 1
            for c in d1:
                if d1[c] != d2[c]:
                    break
            else:
                return True
            d2[s2[i - len(s1) + 1]] -= 1
        return False

sol = Solution()
s1 = "ab"
s2 = "eidbcaooo"
print(sol.checkInclusion(s1,s2))
