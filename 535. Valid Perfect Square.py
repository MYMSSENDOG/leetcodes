class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        m = len(str(num))
        l = 1
        r = int("9" * (m // 2 + 1))
        while l < r:
            m = (l + r) // 2
            if m * m == num:
                return True
            elif m * m > num:
                r = m
            else:
                l = m+1
        return False

sol = Solution()
num = 1
print(sol.isPerfectSquare(num))