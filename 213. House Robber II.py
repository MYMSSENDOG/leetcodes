class Solution:
    def rob(self, nums) -> int:
        if len(nums) <= 3:
            return max(nums)
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[:2])

        dp2 = [0] * len(nums)
        dp2[1] = nums[1]
        ret = 0

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        ret = max(ret, dp[-2])

        for i in range(2, len(nums)):
            dp2[i] = max(dp2[i - 2] + nums[i], dp2[i - 1])
        ret = max(ret, dp2[-1])
        return ret

sol = Solution()
nums = [2,1,1,2]
print(sol.rob(nums))