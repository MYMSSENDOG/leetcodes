class Solution:
    def numOfArrays(self, n: int, m: int, k: int):

        dp = [[[0]* (k + 1) for i in range(n + 1)] for _ in range(m + 1)]

        for l in range(1, n + 1):
            for _k in range(1,k + 1):
                for hi in range(1,m+1):
                    if _k == 1:
                        dp[hi][l][_k] = hi ** (l - 1)
                    else:
                        dp[hi][l][_k] += dp[hi][l - 1][_k] * hi
                        for _hi in range(1,hi):
                            dp[hi][l][_k] += dp[_hi][l - 1][_k - 1]
        ret = 0
        for i in range(1,m+1):
            ret += dp[i][n][k] % (10 ** 9 + 7)
        return ret % (10 ** 9 + 7)




sol = Solution()
n = 2
m = 3
k = 1
print(sol.numOfArrays(n,m,k))