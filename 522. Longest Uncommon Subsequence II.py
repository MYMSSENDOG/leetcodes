import collections
class Solution:
    def findLUSlength(self, strs) -> int:
        d = collections.defaultdict(list)
        strs.sort()
        for s in strs:
            m = len(s)
            d[m] += [s]

        for i in range(10,0,-1):
            if len(d[i]) == 1:
                return i
            elif not d[i]:
                continue

            d2 = collections.defaultdict(int)
            for sb in d[i]:
                d2[sb] +=1
            for sb in d[i]:
                if d2[sb] == 1:
                    return i

        return -1








sol = Solution()
strs = ["aba", "cdc", "eae"]
print(sol.findLUSlength(strs))