class Solution:
    def singleNumber(self, nums) -> int:
        for i in range(1,len(nums)):
            nums[0] ^= nums[i]
        return nums[0]
sol = Solution()
nums = [2,2,1]
print(sol.singleNumber(nums))