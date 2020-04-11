class Solution:
    def createTargetArray(self, nums, index):
        ret = []
        for i , e in enumerate(index):
            ret.insert(e, nums[i])
        return ret
sol = Solution()

nums = [0,1,2,3,4]
index = [0,1,2,2,1]
print(sol.createTargetArray(nums,index))