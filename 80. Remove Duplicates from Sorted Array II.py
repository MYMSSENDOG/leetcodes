class Solution:
    def removeDuplicates(self, nums) -> int:

        i = 0
        j = 0
        pre_i = 0
        while i < len(nums):
            prev = nums[i]
            pre_i = i
            while  i + 1 < len(nums) and nums[i+1] == prev:
                i += 1
            if i -pre_i + 1>0:
                nums[j] = prev
                j+=1
            if i-pre_i + 1>1:
                nums[j] = prev
                j+=1
            i+=1
        print(nums[:j])
        return j

sol = Solution()
nums = [0,0,0,1,1,2]
print(sol.removeDuplicates(nums))