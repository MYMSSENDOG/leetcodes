class Solution:
    def find132pattern(self, nums) -> bool:
        n = len(nums)
        if n < 3:
            return False
        min_dp = [0] * n
        min_dp[0] = -1
        min_dp[1] = 0#svaing index
        previous_greater = [0] * n
        stack = []
        for i in range(2,n):
            idx = min_dp [i-1]
            if nums[i-1] < nums[idx]:
                min_dp[i] = i-1
            else:
                min_dp[i] = idx

        for i in range(n-1,-1,-1):
            if not stack:
                stack.append(i)
                continue
            cur = nums[i]
            idx = stack[-1]
            if cur <= nums[idx]:
                stack.append(i)
            else:
                while stack and nums[idx] < cur:
                    stack.pop(-1)
                    previous_greater[idx] = i
                    if stack:
                        idx = stack[-1]
                stack.append(i)

        for idx in stack:
            previous_greater[idx] = -1
        for i in range(2,n):
            idx3 = previous_greater[i]
            idx1 = min_dp[idx3]
            if idx1 != -1 and idx3 != - 1 and nums[idx1]< nums[i]:
                return True
            else:
                continue
        return False
        #TODO r이전의 가장 먼 nums[r]보다 작은idx 를 찾을 수 있는지 O(n)으로


sol = Solution()
nums = [3,5,0,3,4]
print(sol.find132pattern(nums))