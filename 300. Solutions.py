class Solution:
    def lengthOfLIS(self, nums) -> int:
        n = len(nums)
        dp = [0] * n
        for i in range(n):
            if dp[i] == 0:
                dp[i] =1
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
        return max(dp)

sol = Solution()
nums = [10,9,2,5,3,7,101,18]
print(sol.lengthOfLIS(nums))