class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return (num & (-num) == num) and (num - 1) % 3 == 0

sol = Solution()
num = 64
print(sol.isPowerOfFour(num))