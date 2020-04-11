class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        i = 0
        while 1:
            cur = 3 ** i
            if cur == n:
                return True
            if cur > n:
                return False
            i += 1
sol = Solution()
n = 45
print(sol.isPowerOfThree(n))