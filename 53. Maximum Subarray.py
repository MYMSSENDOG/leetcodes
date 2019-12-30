class Solution:
    def maxSubArray(self, nums) -> int:
        if len(nums) == 0:
            return
        maximum = nums[0]
        sum = nums[0]
        for i in range(1, len(nums)):
            sum = sum + nums[i] if sum > 0 else nums[i]
            maximum = max(maximum,sum)
        return maximum

nums = [-1,-2]
sol = Solution()
print(sol.maxSubArray(nums))