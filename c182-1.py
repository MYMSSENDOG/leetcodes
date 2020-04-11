import collections
class Solution:
    def findLucky(self, arr) -> int:
        d = collections.defaultdict(int)
        ret = -1
        for i in arr:
            d[i] +=1
        for i, e in d.items():
            if i == e:
                ret = max(ret, i)
        return ret

sol = Solution()
arr = [1,2,3,4]
print(sol.findLucky(arr))