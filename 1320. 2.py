class Solution:
    def minimumDistance(self, word: str) -> int:
        def d(a, b):
            return a and abs((a-1) // 6 - (b-1) // 6) + abs((a-1) % 6 - (b-1) % 6)
        dp = [[[9999]* 27 for _ in range(27)]for a in range(len(word) + 1)]

        q= {(0,0):1}
        q2 = {}
        dp[-1][0][0] = 0
        for i, c in enumerate((ord(c) - 64 for c in word)):
            n = len(q)
            for l, r in q:

                dp[i][l][c] = min(min(dp[i-1][l][c], 3000), dp[i-1][l][r] + d(r,c), dp[i][l][c])
                dp[i][c][r] = min(min(dp[i - 1][c][r], 3000), dp[i - 1][l][r] + d(l, c), dp[i][c][r])
                q2[(l,c)] = 1
                q2[(c, r)] = 1
            q = q2
            q2 = {}
        return min(dp[-2][z][x] for z, x in q )


sol = Solution()
word = "YEAR"
print(sol.minimumDistance(word))
