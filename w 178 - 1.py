import copy
class Solution:
    def smallerNumbersThanCurrent(self, nums):
        s = copy.deepcopy(nums)
        nums.sort()
        d = {}
        d[nums[0]] = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                d[nums[i]] = i
        ret = [0] * len(nums)
        for i in range(len(nums)):
            ret[i] = d[s[i]]
        return ret
sol = Solution()
nums = [6,5,4,8]
print(sol.smallerNumbersThanCurrent(nums))
"""
import copy
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        s = copy.deepcopy(nums)
        nums.sort()
        d = {}
        d[nums[0]] = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                d[nums[i]] = i
        ret = [0] * len(nums)
        for i in range(len(nums)):
            ret[i] = d[s[i]]
        return ret         

"""