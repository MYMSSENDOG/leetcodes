import collections
class Solution:
    def topKFrequent(self, nums, k: int) :
        d = collections.defaultdict(int)
        f = collections.defaultdict(list)
        for i in nums:
            d[i] +=1
        for q, v in d.items():
            f[v]+=[q]
        ret = []
        n = len(nums)
        while len(ret)<k:
            if n in f:
                ret += f[n]
            n-=1
        return ret

nums = [5,2,5,3,5,3,1,1,3]
k = 2
sol = Solution()
print(sol.topKFrequent(nums,k))