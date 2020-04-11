class Solution:
    def productExceptSelf(self, nums):
        if not nums or len(nums) == 1:
            return nums

        ret = [1] * len(nums)

        ret[-1] = nums[-1]
        for i in reversed(range(len(ret)-1)):
            ret[i] = nums[i] * ret[i + 1]
        i = 0
        ret[-1] = 1
        while i < len(nums) - 2:
            ret[i] = ret[i+1] * ret[-1]
            ret[-1] *= nums[i]
            i+=1
        ret[-2] = ret[-1] * nums[-1]
        ret[-1] = ret[-1] * nums [-2]
        return ret

sol = Solution()
nums = [1,2,3,4]
print(sol.productExceptSelf(nums))