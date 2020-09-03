import heapq
class Solution:
    def change(self, amount: int, coins):
        if amount == 0:
            return 1
        if not coins or min(coins) > amount:
            return 0
        m = len(coins)
        dp = [[0] * m for _ in range(amount + 1)]  #dp[coin][amount]
        for i,c in enumerate(coins):
            if c <= amount :
                dp[c][i] = 1
        for cur in range(amount):
            for i in range(m):
                for j in range(i, m):
                    if cur + coins[j] <= amount:
                        dp[cur + coins[j]][j]+=dp[cur][i]
        return sum(dp[-1])



sol = Solution()
amount = 5
coins = []
print(sol.change(amount, coins))