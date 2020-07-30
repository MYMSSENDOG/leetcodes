import collections
class Solution:
    def frequencySort(self, s: str) -> str:
        d1 = collections.defaultdict(int)
        d2 = collections.defaultdict(list)
        m = 0
        for c in s:
            d1[c] +=1
            m = max(d1[c], m)
        for c in d1:
            d2[d1[c]] += [c]

        ret = ""
        for i in range(m,0,-1):
            for c in d2[i]:
                ret += c * i
        return ret
sol = Solution()
s = "aaabbbcdddd"
print(sol.frequencySort(s))

