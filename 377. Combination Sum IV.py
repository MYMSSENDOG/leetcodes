class Solution:
    def combinationSum4(self, nums, target: int) -> int:

        def dfs(i, cur):
            if cur == target:
                return 1
            if cur>target:
                return 0
            ret = 0
            for k in range(0, len(nums)):
                ret += dfs(k, cur + nums[k])
            return ret
        return dfs(0,0)
sol = Solution()
nums = [1, 2, 3]
target = 4
print(sol.combinationSum4(nums,target))