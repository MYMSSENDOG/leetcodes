from tree_node_lib import *
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[0] = 1
        if n == 0:
            return 0
        else:
             for i in range(1,n+1):
                for j in range(i):
                    dp[i] += dp[j] * dp[i-j-1]
        return dp[n]
sol = Solution()
n = 5
print(sol.numTrees(n))
