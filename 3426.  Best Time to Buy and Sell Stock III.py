class Solution:
    def maxProfit(self, prices) -> int:
        n = len(prices)
        if not prices:
            return 0
        m = prices[0]
        M = prices[-1]
        dp1 = [0] * n
        dp2 = [0] * n
        for i in range(1, n):
            p = prices[i]
            m = min(m, p)
            dp1[i] = max(dp1[i-1], p - m)

        for i in range(n - 1)[::-1]:
            p = prices[i]
            M = max(M, p)
            dp2[i] = max(dp2[i+1], M - p)

        return max(dp1[i] + dp2[i] for i in range(n))



sol = Solution()
prices = [1,2,3,4,5]
print(sol.maxProfit(prices))