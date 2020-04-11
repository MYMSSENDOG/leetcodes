class Solution:
    def wiggleMaxLength(self, nums) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        up = 0
        ret = 1
        for i in range(1, len(nums)):
            dif = nums[i] - nums[i-1]
            if dif == 0:
                continue
            elif dif> 0:
                if up ==1:
                    continue
                else:
                    up = 1
                    ret +=1
            elif dif < 0:
                if up == 1 or up == 0:
                    ret +=1
                    up = -1
                else:
                    continue
        return ret


sol = Solution()
nums = [1,17,5,10,13,15,10,5,16,8]
print(sol.wiggleMaxLength(nums))