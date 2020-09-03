class Solution:
    def mincostTickets(self, days, costs) -> int:
        r30 = 0
        r7= 0
        dp = [float("inf")] * (len(days) + 1)
        dp[-1] = 0
        for i in range(len(days)):
            while r30 < len(days) and  days[i] + 29 >= days[r30]:
                dp[r30] = min(dp[i - 1] + costs[2], dp[r30])
                r30 += 1

            while r7 < len(days) and days[i] + 6 >= days[r7]:
                dp[r7] = min(dp[i - 1] + costs[1], dp[r7])
                r7 += 1
            dp[i] = min(dp[i - 1] + costs[0], dp[i])
        return dp[-2]

sol = Solution()
days = [1,2,3,4,5,6,7,8,9,10,30,31]
costs = [2,7,15]
print(sol.mincostTickets(days, costs))