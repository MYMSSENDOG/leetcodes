class Solution:
    def majorityElement(self, nums) -> int:
        major = nums[0]
        count = 1
        for i in nums[1:]:

            if i == major:
                count += 1
            elif count == 0:
                major = i
                count = 1
            else:
                count -= 1
        return major
sol = Solution()
nums = [3,2,3]
print(sol.majorityElement(nums))