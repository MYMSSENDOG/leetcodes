class Solution:
    def maxProfit(self, prices) -> int:
        l = len(prices)
        s0 = [0] * l            # can buy
        s1 = [0] * l            # after buy
        s2 = [0] * l          # after sell
        s1[0] = - prices[0]
        s2[0] = -999999
        for i, p in enumerate(prices[1:], 1):
            s0[i] = max(s0[i-1], s2[i-1])
            s1[i] = max(s0[i-1] - p, s1[i-1])
            s2[i] = s1[i-1] + p
        return max(s0[-1], s2[-1])


prices = [1,2,3,0,2]
sol = Solution()
print(sol.maxProfit(prices))