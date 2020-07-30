class Solution:
    def arrangeCoins(self, n: int) -> int:
        # r^2 + r <= 2n < r^2 + 3r + 2
        r = int((n*2) **(1/2))
        while not ((r*(r+1) <= 2*n) and ((r+1) * (r+2)> 2 * n)):
            r-=1
        return r


n = 10
sol = Solution()
print(sol.arrangeCoins(n))