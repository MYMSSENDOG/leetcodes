class Solution:
    def singleNonDuplicate(self, nums) -> int:
        l = 0
        r = len(nums)
        while l < r:
            m = (l + r)//2
            if m == 0 or m == len(nums) - 1:
                return nums[m]
            if m % 2 == 0:
                if nums[m] == nums[m+1]:
                    l = m+2
                elif nums[m] == nums[m-1]:
                    r = m-1
                else:
                    return nums[m]
            elif m%2 == 1:
                if nums[m] == nums[m - 1]:
                    l = m+1
                elif nums[m] == nums[m + 1]:
                    r = m
                else:
                    return nums[m]
        return nums[l]
sol = Solution()
nums = [3,3,7,7,10,11,11]
print(sol.singleNonDuplicate(nums))
"""

abcde
abde
110098794
100987894
4295

"""
