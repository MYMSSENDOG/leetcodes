class Solution:
    def integerBreak(self, n: int) -> int:
        memo = {1:0, 2: 1}# 분해 했을때 최대값
        def dfs(n):
            if n in memo:
                return memo[n]
            else:
                ret = 0
                for i in range(1, n//2+1):
                    ret = max(ret, max(dfs(i),i ) * max(n-i, dfs(n-i)))#분해했을 때 or 고대로 했을 때
                memo[n] = ret
                return ret
        return dfs(n)

sol = Solution()
n = 10
print(sol.integerBreak(n))