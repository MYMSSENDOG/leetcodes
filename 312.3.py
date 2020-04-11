class Solution:
    def maxCoins(self, nums) -> int:


        nums = [1] + [i for i in nums if i > 0] + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for k in range(2, n):
            for l in range(0, n-k):
                r = l + k
                dp[l][r] = max(dp[l][m] + dp[m][r] + nums[m] * nums[l] * nums[r] for m in range(l+1, r))
        return dp[0][-1]








sol = Solution()
nums = [2,3,3]
print(sol.maxCoins(nums))