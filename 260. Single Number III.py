class Solution:
    def singleNumber(self, nums):
        t = 0
        for i in nums:
            t ^= i
        a, b = 0,0
        c = t & -t
        for i in nums:
            if i & c ==0:
                a ^= i
            else:
                b ^= i
        return [a, b]


sol = Solution()
nums = [1,2,1,3,2,5]
print(sol.singleNumber(nums))