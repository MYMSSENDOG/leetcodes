class Solution:
    def containsDuplicate(self, nums) -> bool:
        dict = {}
        for i in nums:
            if i in dict:
                return True
            else:
                dict[i] = 0
        return False
sol = Solution()
nums = [1.2,3.1]
print(sol.containsDuplicate(nums))