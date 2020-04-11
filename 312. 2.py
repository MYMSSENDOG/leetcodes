class Solution:
    def maxCoins(self, nums) -> int:
        d = {}
        def memo(l, r):
            ret = 0
            if (l,r) in d:
                return d[(l,r)]
            if r - l == 2:
                return nums[r] * nums[l] * nums[l+1]
            elif r - l < 2:
                return 0
            else:
                ret = max(memo(l, m) + nums[l] * nums[m] * nums[r] + memo(m,r) for m in range(l+1,r))
            d[(l,r)] = ret
            return ret


        nums = [1] + [i for i in nums if i > 0] + [1]
        n = len(nums)
        return memo(0,n-1)








sol = Solution()
nums = [2,3,3]
print(sol.maxCoins(nums))