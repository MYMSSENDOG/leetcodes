class Solution:
    def longestConsecutive(self, nums) -> int:
        nums.sort()
        start = 0
        end = 0
        r_s = 0
        r_e = 0

        for i in range(1,len(nums)):
            if nums[i] -1 == nums[i-1] or nums[i] == nums[i-1]:
                end +=1
            else:
                start = i
                end = i
            if nums[start] -nums[end] < nums[r_s]-  nums[r_e]:
                r_s = start
                r_e = end
        return - nums[r_s] + nums[r_e] + 1
sol = Solution()
nums = [100, 4, 200, 1, 3, 2]
print(sol.longestConsecutive(nums))