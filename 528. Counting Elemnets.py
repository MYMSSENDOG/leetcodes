import collections
class Solution:
    def countElements(self, arr) -> int:
        d = collections.defaultdict(int)
        for i in arr:
            d[i] +=1
        return sum(e for c, e in d.items() if c+1 in d)

sol = Solution()
arr = [1,2,2,1]
print(sol.countElements(arr))