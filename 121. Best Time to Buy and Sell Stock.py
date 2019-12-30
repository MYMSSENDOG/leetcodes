class Solution:
    def maxProfit(self, prices) -> int:
        min_price = 9999999
        ret = 0
        for i in prices:
            if i < min_price:
                min_price = i
            elif i - min_price > ret:
                ret = i - min_price
        return ret
sol = Solution()
prices = [2,1,2,1,0,1,2]
print(sol.maxProfit(prices))