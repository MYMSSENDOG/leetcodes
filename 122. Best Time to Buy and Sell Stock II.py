class Solution:
    def maxProfit(self, prices) -> int:
        descending = True
        buy = 0
        sell = 0
        ret = 0
        for i in range(len(prices)-1):
            if descending:
                if prices[i] > prices[i+1]:
                    continue
                else:
                    descending = False
                    buy = prices[i]
            else:
                if prices[i] < prices[i + 1]:
                    continue
                else:
                    sell =prices[i]
                    ret += sell - buy
                    descending = True
        if not descending and prices[-1] - buy >0:
            ret+=prices[-1] - buy
        return ret

sol = Solution()
prices = [7,1,5,3,6,4]
print(sol.maxProfit(prices))