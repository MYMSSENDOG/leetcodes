class Solution:
    def minSubsequence(self, nums):
        s = sum(nums)
        nums.sort(reverse= True)
        t = 0
        ret = []
        for i in nums:
            t +=i
            s -=i
            ret.append(i)
            if t>s:
                return ret
sol = Solution()
nums = [4,3,10,9,8]
print(sol.minSubsequence(nums))