class Solution:
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return left
sol = Solution()
nums = [1,3,4,6]
target = 5
print(sol.searchInsert(nums,target))