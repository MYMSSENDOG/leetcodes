class Solution:
    def minStartValue(self, nums) -> int:
        cur = 0
        ret = float('inf')
        for i in nums:
            cur += i
            ret = min(ret, cur)
        return max(-ret + 1, 1)


sol = Solution()
nums = [1,-2,-3]
print(sol.minStartValue(nums))