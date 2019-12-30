class Solution:
    def searchRange(self, nums, target) :
        left = 0
        right = len(nums) - 1
        ret = []

        if not nums:
            return [-1,-1]
        while left<right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1

        if nums[left] == target:
            ret.append(left)
        else:
            return [-1,-1]
        right = len(nums) - 1

        while left < right:
            mid = int((left + right+1) / 2)
            if nums[mid] <= target:
                left = mid
            else:
                right = mid - 1
        ret.append(right)
        return ret


nums = [0,]
target = 0
sol = Solution()
print(sol.searchRange(nums, target))




