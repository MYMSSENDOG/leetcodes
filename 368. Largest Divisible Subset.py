
class Solution:
    def largestDivisibleSubset(self, nums):
        if not nums:
            return []
        dp = [[0,[]] for _ in range(len(nums))]

        nums.sort()

        #all index
        for i in range(len(nums)):
            if not dp[i][1]:
                dp[i][1] = [nums[i]]
            for j in range(i+1, len(nums)):
                if nums[j] % nums[i] == 0:
                    dp[j] = max([dp[i][0] + 1, dp[i][1] + [nums[j]]], dp[j])
        return max(dp)[1]


nums = [1,2,4,8,3,9,27,81,243,5,25,125,6,12]
sol = Solution()
print(sol.largestDivisibleSubset(nums))