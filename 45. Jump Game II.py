class Solution:
    def jump(self, nums):
        if len(nums)<= 1:
            return 0
        step  = 1
        l = 0
        reachable = nums[0]
        while reachable < len(nums)-1:
            step += 1
            maxd = max(i + nums[i] for i in range(l, reachable + 1))
            l = reachable
            reachable = maxd
        return step
# code under is dp solution but dp is not good at this problem
"""
        valid_index = [0]
        dp = [0] * len(nums)
        for i in range(1, len(nums)):
            mind = 99999
            for j in valid_index:
                mind = min(mind, dp[j] + 1)

            for j in range(i):
                if nums[j]>= i-j:
                    mind = min(mind, dp[j] + 1)                     

            dp[i] = mind
            if nums[i] >=1:
                valid_index.append(i)
            for k in reversed(range(len(valid_index))):
                if nums[valid_index[k]] + valid_index[k]<i+1:
                    del(valid_index[k])
        return dp[len(nums)-1]
"""




n = [2,3,1,1,4]
sol = Solution()
print(sol.jump(n))