
class Solution:
    def find132pattern(self, nums) -> bool:
        smallest = float('inf')
        stack = []
        for i in nums:
            while stack and i >= stack[-1][-1]:
                stack.pop()
            if stack and i > stack[-1][0]:
                return True
            stack.append((smallest, i))
            smallest = min(smallest, i)
        return False


sol = Solution()
nums = [4,5,3,4,2,3,1,2,0,1]
print(sol.find132pattern(nums))