import collections
class Solution:
    def minSetSize(self, arr) -> int:
        d = collections.defaultdict(int)
        if not arr:
            return 0
        n = len(arr)
        for i in arr:
            d[i] += 1
        ret = []
        for e in d:
            ret.append(d[e])
        ret.sort()
        total = 0
        prev= -141424
        t = 0
        for i  in reversed(range(len(ret))):
            total += ret[i]
            t +=1
            if total>= n // 2:
                return t

sol = Solution()
arr = [1.1,3,7]
print(sol.minSetSize(arr))