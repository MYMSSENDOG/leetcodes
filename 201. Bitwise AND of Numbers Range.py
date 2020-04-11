class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        a = m
        b = n
        count = 0
        while a!=b:
            a = a//2
            b = b//2
            count +=1
        return a * 2 ** count




m = 0
n = 1
sol  = Solution()
print(sol.rangeBitwiseAnd(m,n))