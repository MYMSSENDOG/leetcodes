class Solution:
    def minSubArrayLen(self, s: int, nums) -> int:
        if not nums:
            return 0
        m = 9999
        l = 0
        r = 1
        cur = nums[0]
        while r < len(nums)+1:
            if cur < s:
                if r == len(nums):
                    break
                cur += nums[r]
                r += 1
            elif cur >= s:
                m = min(m, r - l)
                ###
                if m == 1:
                    return 1
                ###
                cur -= nums[l]
                l += 1
        return 0 if m == 9999 else m

s = 7
nums = [2,3,1,2,4,3]
sol = Solution()
print(sol.minSubArrayLen(s,nums))