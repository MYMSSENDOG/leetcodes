class Solution:
    def maxProfit(self, prices) -> int:
        """
        prices is identical price rise
        every price rise, we buy it low and sell it peak
        compare former peak - second low and former peak - 1 - first low
        and choose the bigger one

        s1 O(n^2)
        get the profit buy in i , sell in j
        for k in range(n)
            dp[k] = max(dp[p]
        
        """
        #생각할 수 있는 기능
        #1. best profit with one or less transaction between i to j
        s0 = 0
        s1 = -prices[0]
        s2 = -9999
        for i, p in enumerate(prices[1:],1):
            t0 = s0
            t1 = s1
            s0 = max(s0, s2)
            s1 = max(s1, t0 - p)
            s2 = t1 + p
        return max(s2,s0)

sol = Solution()
prices = [2,1]
print(sol.maxProfit(prices))