import sys
class Solution:
    def maximumGap(self, nums) -> int:
        n = len(nums)
        M = max(nums)
        m = min(nums)
        if  n == 0 or n == 1:
            return 0

        Mvalues = [-sys.maxsize-1] * (n+1)
        mvalues = [sys.maxsize] * (n+1)
        l = (M - m)/(n-1)
        if l == 0:
            return 0
        for i in nums:
            idx = int((i - m) // l)
            Mvalues[idx] = max(Mvalues[idx], i)
            mvalues[idx] = min(mvalues[idx],i)
        gap = 0
        pre = Mvalues[0]
        for i in range(1,n):
            if mvalues[i] == sys.maxsize:
                continue
            else:
                gap = max(gap, mvalues[i] - pre)
                pre = mvalues[i]
        return gap


sol = Solution()
nums = [1,1,1,1,5,5,5,5]
print(sol.maximumGap(nums))