
class Solution:
    def subarraySum(self, nums, k: int) -> int:
        d = {0:1}
        t = 0
        ret = 0
        for i in nums:
            t += i
            if t - k in d:
                ret += d[t-k]
            d[t] = d[t] + 1 if t in d else 1
        return ret
        #return sum(d[i] * d[i-k] for i in d if i-k in d) + d[k]




sol = Solution()
nums = [1,1,1,1,1]
k = 2
print(sol.subarraySum(nums,k))