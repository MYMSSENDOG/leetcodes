class Solution:
    def maxUncrossedLines(self, A, B) -> int:
        m = len(A)
        n = len(B)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                if A[i] == B[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        return dp[-2][-2]
sol = Solution()
A = [2,5,1,2,5]
B = [10,5,2,1,5,2]
print(sol.maxUncrossedLines(A,B))