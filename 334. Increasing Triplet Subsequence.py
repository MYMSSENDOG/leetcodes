class Solution:
    def increasingTriplet(self, nums) -> bool:
        if len(nums) < 3:
            return False
        min = nums[0]
        second = None
        for i in range(1,len(nums)):
            if second == None:
                if nums[i] <= min:
                    min = nums[i]
                else:
                    second = nums[i]
            else:
                if nums[i] > second:
                    return True
                elif nums[i]<min:
                    min = nums[i]
                elif nums[i] < second and min< nums[i]:
                    second = nums[i]
        return False


sol = Solution()
nums = [1,0,-1,0,100]
print(sol.increasingTriplet(nums))