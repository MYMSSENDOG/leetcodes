class Solution:
    def findDuplicates(self, nums):
        ret = []
        for i, e in enumerate(nums):
            if e- 1 < len(nums):
                nums[e-1] += len(nums)
            elif e-1 < 2 * len(nums):
                nums[e - 1 - len(nums)] += len(nums)
            else:
                nums[e - 1 - 2 * len(nums)] += len(nums)
        for i,e  in enumerate(nums):
            if e > 2 * len(nums):
                ret.append(i+1)
        return ret

sol = Solution()
nums = [3,4,2,7,8,2,3,1]
print(sol.findDuplicates(nums))
"""

현재i번 n임
만약 nums[n-1] == 0 이면
    ret에 추가
아니면
    다음에 볼거 nums[nums[n-1]] - 1
    nums[n-1] = 0

"""