class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        nums.sort()
        return nums[-k]

nums = [3,2,3,1,2,4,5,5,6]
sol = Solution()
print(sol.findKthLargest(nums))