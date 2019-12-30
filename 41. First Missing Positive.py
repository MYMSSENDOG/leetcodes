class Solution:
    def firstMissingPositive(self, nums):
        dic = {}
        for i in nums:
            if i <1:
                continue
            else:
                dic[i] = 1
        for i in range(1, len(nums)+1,1):
            if i not in dic:
                return i
        return len(nums)+1

sol = Solution()
nums = [1,2]
print(sol.firstMissingPositive(nums))