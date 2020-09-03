class Solution:
    def nextGreaterElements(self, nums):

        n = len(nums)
        if not n:
            return []
        ret = [-1] * n
        nums = nums * 2
        nums.pop()
        stack = []
        for i in range(2*n-2, n-1,-1):
            while stack and stack[-1] < nums[i]:
                stack.pop()
            if not stack:
                stack.append(nums[i])
            elif stack and nums[i]<stack[-1]:
                stack.append(nums[i])
        for i in range(n-1, -1,-1):
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            if not stack:
                stack.append(nums[i])
                ret[i] = -1
            elif stack and nums[i]<stack[-1]:
                ret[i] = stack[-1]
                stack.append(nums[i])
        return ret


sol = Solution()
nums = [1,2,1]
print(sol.nextGreaterElements(nums))