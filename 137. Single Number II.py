class Solution:
    def singleNumber(self, nums) -> int:
        """
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
        """
        if len(nums) == 1:
            return nums[0]

        nums[0] ^= nums[1]
        nums[1] = 0 ^ ((nums[0]^nums[1]) & nums[1])

        nums[1] = nums[1] ^ (nums[0] & nums[2])
        nums[0] ^= nums[2]

        nums[2] = ~ (nums[0] & nums[1])
        nums[1] = nums[1] & nums[2]

        nums[0] = nums[0] & nums[2]

        for i in nums[3:]:
            nums[1] = nums[1] ^ (nums[0] & i)
            nums[0] ^= i
            nums[2] = ~ (nums[0] & nums[1])
            nums[1] = nums[1] & nums[2]
            nums[0] = nums[0] & nums[2]
        return nums[0]
sol = Solution()
nums = [0,1,0,1,0,1,99]
print(sol.singleNumber(nums))