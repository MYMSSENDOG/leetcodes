class Solution:
    def canWinNim(self, n: int) -> bool:
        return n %4 ==1
sol = Solution()
n = 6
print(sol.canWinNim(n))