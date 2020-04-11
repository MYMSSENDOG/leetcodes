class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 1
        r = 2**16
        while l < r:
            m = (l + r) // 2
            cur = m**2
            if cur == num:
                return True
            elif cur > num:
                r = m
            else:
                l = m+1
        return False

sol = Solution()
num = 16
print(sol.isPerfectSquare(num))