class Solution:
    def PredictTheWinner(self, nums):
        n = len(nums)
        dp = [[0] * (n+1) for _ in range(n+1)]
        for i in range(n-1,-1,-1):
            for j in range(i+1):
                l = j
                r = i-j
                dp[l][r] = max(nums[l] - dp[l+1][r], nums[-r-1] - dp[l][r + 1])
        return dp[0][0] >= 0


sol = Solution()
nums = [1,5,233,7]
print(sol.PredictTheWinner(nums))