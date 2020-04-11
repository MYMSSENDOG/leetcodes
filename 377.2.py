class Solution:
    def combinationSum4(self, nums, target: int) -> int:
        memo = {target:1}# numsber of ways to go target to target
        def helper(cur):
            if cur in memo:
                return memo[cur]
            if cur>target:
                return 0

            ret = 0
            for i in range(len(nums)):
                ret += helper(cur + nums[i])
            memo[cur] =ret
            return ret
        return helper(0)


sol = Solution()
nums = [1, 2, 3]
target = 4
print(sol.combinationSum4(nums,target))