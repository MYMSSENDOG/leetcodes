import bisect
class Solution:
    def coinChange(self, coins, amount: int) -> int:
        dp = [-1] * (amount+1)
        dp[0] = 0
        n = len(coins)
        coins.sort()
        q = [[coins[0], 0]]
        while q[0][0] <= amount:
            val, s_id = q.pop(0)
            if dp[val] == -1:
                dp[val] = dp[val - coins[s_id]]+1
            else:
                dp[val] = min(dp[val], dp[val - coins[s_id]]+1)

            if s_id == n - 1:
                q.append([val + coins[s_id], s_id])
                continue
            bisect.insort(q, [val + coins[s_id], s_id])
            bisect.insort(q, [val + coins[s_id+1] - coins[s_id], s_id+1])



        return dp[-1]

# TLE

sol = Solution()
coins = [186,419,83,408]

amount = 6249

print(sol.coinChange(coins, amount))