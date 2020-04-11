class Solution:
    def coinChange(self, coins, amount: int) -> int:
        memo = {}
        m = min(coins)
        def dfs(amount):
            if amount in memo:
                return memo[amount]
            if amount in coins:
                return 1
            if not amount:
                return 0
            if amount < m[0] and amount not in coins:
                return -1
            ret = -1
            for c in coins:
                t = dfs(amount-c)
                if t == -1:
                    continue
                elif ret == -1:
                    ret = t + 1
                else:
                    ret = min (ret, t +1)
            memo[amount] =  ret
            return  ret
        return dfs(amount)

sol = Solution()
coins = [83,474,400,3]
amount = 264

print(sol.coinChange(coins, amount))