class Solution:
    def numberOfSubarrays(self, nums, k: int) -> int:
        odd = []
        if k == 0:
            return 2 ** len(nums)
        for i in range(len(nums)):
            if nums[i] %2 == 1:
                odd.append(i)
        if k > len(odd):
            return 0
        ret = 0
        for i in range(k-1,len(odd)):
            end = odd[i]
            start = odd[i - k + 1]
            if len(odd)>i+1:
                r_pens = odd[i+1]
            else:
                r_pens = len(nums)
            if i>=k:
                l_pens = odd[i - k ]
            else:
                l_pens = -1
            ret += (start - l_pens ) * (r_pens - end)
        return ret

sol = Solution()
nums = [1,2,1,2,1,2,1,2]
k = 1
print(sol.numberOfSubarrays(nums,k))