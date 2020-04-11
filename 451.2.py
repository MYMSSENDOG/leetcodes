import collections
class Solution:
    def frequencySort(self, s: str) -> str:

        d = collections.defaultdict(int)
        for c in s:
            d[c] +=1
        A = [[i, e] for i, e in d.items()]
        A.sort(key = lambda count:count[1], reverse = True)
        ret = ""
        for c, i in A:
            ret += c * i
        return ret 

sol = Solution()
s = "tree"
print(sol.frequencySort(s))