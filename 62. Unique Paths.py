class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ret = 1
        c = m + n - 2
        step = 1
        for i in range(min(m-1,n-1)):
            ret *= c
            c-=1
            ret = ret //step
            step += 1
        return ret
sol = Solution()
m = 4
n = 3
print(sol.uniquePaths(m,n))