class Solution:
    def findPeakElement(self, nums) -> int:
        if len(nums) == 1:
            return 0
        p = 0
        l = 1
        r = len(nums)-1
        m = (l + r)//2
        while l+1<r:
            m = (l + r)//2
            if nums[m] < nums[p]:
                r = m
            elif nums[m] > nums[p]:
                l = m
            else:
                return max(self.findPeakElement(nums[:m]),self.findPeakElement(nums[m:]))
        if max(nums[m],nums[p], nums[r]) == nums[m]:
            return m
        elif max(nums[m],nums[p], nums[r]) == nums[p]:
            return p
        else:
            return r

sol = Solution()
nums = [1,3,2,1]
print(sol.findPeakElement(nums))