import copy

def per(nums, index, ret, temp):
    if len(nums) == 0:
        b = copy.deepcopy(temp)
        ret.append(b)
        return
    for i in range(len(nums)):
            temp.append(nums[i])
            per(nums[:i] + nums[i+1:] , index, ret, temp)
            temp.pop()

class Solution:
    def permute(self, nums):
        ret = []
        index = [False] * len(nums)
        per(nums,index,ret,[])
        return ret

sol = Solution()
n = [1,2,3]
print(sol.permute(n))