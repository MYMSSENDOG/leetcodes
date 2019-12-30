class Solution:
    def removeDuplicates(self, nums) -> int:
        a = set(nums)
        nums = list(a)
        nums = []
        return len(nums)

sol = Solution()
l1 = [1,1,2,2,3,3,3,4,5,6,7]
print(sol.removeDuplicates(l1))
print(l1)
# c++ 로 풀음