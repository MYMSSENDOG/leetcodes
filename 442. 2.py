class Solution:
    def findDuplicates(self, nums):
        ret = []
        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] < 0:
                ret.append(abs(nums[i]))
            else:
                nums[abs(nums[i]) - 1] *= -1
        return ret


"""
constraints
1. numbers is in range(1, n]
2. number appears 0, 1, 2 times only

"""
sol = Solution()
nums = [2,2]
print(sol.findDuplicates(nums))