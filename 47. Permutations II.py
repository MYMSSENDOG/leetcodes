import copy

def per(nums, index, ret, temp):
    if len(nums) == 0:
        b = copy.deepcopy(temp)
        ret.append(b)
        return
    i = 0
    while i < len(nums):
            temp.append(nums[i])
            per(nums[:i] + nums[i+1:] , index, ret, temp)
            i += nums.count(nums[i])
            temp.pop()

class Solution:
    def permuteUnique(self, nums):
        ret = []
        nums.sort()
        index = [False] * len(nums)
        per(nums,index,ret,[])
        return ret

sol = Solution()
n = [1,1,3]
print(sol.permuteUnique(n))