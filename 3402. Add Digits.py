class Solution:
    def addDigits(self, num: int) -> int:
        return (num - 1)%9 + 1

sol = Solution()
num = 38
print(sol.addDigits(num))