class Solution:
    def findDuplicates(self, nums):
        ret = []
        for i, e in enumerate(nums):
            if e- 1 < len(nums):
                nums[e-1] += len(nums)
            elif e-1 < 2 * len(nums):
                nums[e - 1 - len(nums)] += len(nums)
            else:
                nums[e - 1 - 2 * len(nums)] += len(nums)
        for i,e  in enumerate(nums):
            if e > 2 * len(nums):
                ret.append(i+1)
        return ret


"""
constraints 
1. numbers is in range(1, n]
2. number appears 0, 1, 2 times only

"""
sol = Solution()
nums = [4,3,2,7,8,2,3,1]
print(sol.findDuplicates(nums))