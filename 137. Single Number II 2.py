class Solution:
    def singleNumber(self, nums) -> int:

        x2 = 0
        x1 = 0
        mask = 0
        for  i in  nums :
            x2 = x2^(x1 & i)
            x1 ^= i
            mask = ~ (x1 & x2)
            x2 =x2 & mask

            x1 =x1 & mask
        return x1

sol = Solution()
nums = [0,1,0,1,0,1,99]
print(sol.singleNumber(nums))