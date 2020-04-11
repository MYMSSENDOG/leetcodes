class Solution:
    def combinationSum4(self, nums, target: int) -> int:
        nums.sort()
        dp = [1]+[0]*target
        for i in range(target + 1):
            for n in nums:
                if n > i :
                    break
                elif n == i:
                    dp[i] +=1
                else:
                    dp[i] += dp[i - n]
        return dp[-1]


sol = Solution()
nums = [1,2,3]
target = 4

print(sol.combinationSum4(nums,target))