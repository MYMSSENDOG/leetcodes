class Solution:
    def findMin(self, nums) -> int:
        m = nums[0]
        if len(nums) == 1:
            return nums[0]
        l = 1
        r = len(nums)-1
        mid = (r + l)//2
        while l<r - 1:
            mid = (r + l)//2
            if nums[mid] >m:
                l = mid
            else:
                r = mid
        if nums[r] > m:
            ret = (r+1)%len(nums)
        elif nums[l] > m:
            ret = (l+1)%len(nums)
        else:
            ret = l
        return nums[ret]
sol = Solution()
nums = [4,5,1,2,3]
print(sol.findMin(nums))