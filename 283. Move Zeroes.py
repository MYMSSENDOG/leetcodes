class Solution:
    def moveZeroes(self, nums) -> None:
        zero = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                if zero == -1:
                    zero = i
            else:
                if zero == -1:
                    continue
                else:
                    nums[zero] = nums[i]
                    zero +=1
                    nums[i] = 0
        """
        faster version
        zero = 0
        for i in reversed(range(len(nums))):
            if nums[i] == 0:
                nums.pop(i)
                zero +=1
        nums += [0] * zero
        """
        print(nums)
sol = Solution()
nums = [0,1,0,3,12]
sol.moveZeroes(nums)