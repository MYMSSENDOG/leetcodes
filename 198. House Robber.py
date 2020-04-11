class Solution:
    def rob(self, nums) -> int:
        if len(nums)<=2:
            return max(nums)
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[:2])
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        return dp[-1]

sol = Solution()
nums = [4,1,1,4]
print(sol.rob(nums))