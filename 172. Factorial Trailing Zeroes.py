class Solution:
    def trailingZeroes(self, n: int) -> int:
        ret = 0
        while n//5:
            ret += n//5
            n//=5
        return ret
sol = Solution()
n = 10
print(sol.trailingZeroes(n))