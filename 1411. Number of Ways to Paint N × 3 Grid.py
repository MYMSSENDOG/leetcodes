class Solution:
    def numOfWays(self, n: int) -> int:
        x = 6
        y = 6
        for i in range(n - 1):
            x,y  = 2 * x + 2 * y, 2 * x + 3 * y
        return (x + y) % (10 ** 9 + 7)

n = 3
sol = Solution()
print(sol.numOfWays(n))

"""
x = 6
y = 6
for i in range(n - 1):
    x = 2 * x + 2 * y
    y = 2 * x + 3 * y
return (x + y) % (10 ** 9 + 7)
"""