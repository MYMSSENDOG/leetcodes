class Solution:
    def constrainedSubsetSum(self, nums, k: int):
        dp = nums[:]
        stack = [[nums[0],0]] if nums[0] > 0 else []
        for i in range(1, len(nums)):
            if stack and i - stack[0][1] > k:
                stack.pop(0)

            if stack:
                dp[i] = dp[i] + stack[0][0]
            if dp[i] < 0:
                continue
            if not stack:
                stack.append([dp[i], i])
                continue

            if stack and dp[i] >= stack[0][0]:
                stack = [[dp[i], i]]
            else:
                while stack[-1][0] <= dp[i]:
                    stack.pop()
                stack.append([dp[i],i])

        return max(dp)




nums = [-8269,3217,-4023,-4138,-683,6455,-3621,9242,4015,-3790]
k = 1
sol = Solution()
print(sol.constrainedSubsetSum(nums, k))