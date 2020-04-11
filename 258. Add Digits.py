class Solution:
    def addDigits(self, num: int) -> int:

        while num >= 10:
            total = 0
            while num :
                total += num%10
                num //= 10
            num = total
        return num

sol = Solution()
num = 38
print(sol.addDigits(num))