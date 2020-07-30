class Solution:
    def findMin(self, nums) -> int:
        def helper(l, r):
            if l == r:
                return nums[r]
            m = (l + r) // 2
            if nums[l] < nums[m] < nums[r]:
                return nums[l]
            if nums[m] > nums[m+1]:
                return nums[m + 1]

            if nums[r] < nums[m]:
                return helper(m + 1, r)
            elif nums[l] > nums[m]:
                return helper(l, m)
            else:
                left_min = helper(l, m)
                right_min = helper( m + 1 , r)
                return min(left_min, right_min)

        l = 0
        r = len(nums) - 1
        return helper(l, r)

sol = Solution()
nums = [3,3,1,3]
print(sol.findMin(nums))