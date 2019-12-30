class Solution:
    def myPow(self, x: float, n: int) -> float:
        ret = 1
        if n == 0:
            return 1
        if n < 0:
            x = 1/x
            n = -n
        temp  = x

        while n > 1:
            if n%2 == 0:
                x = x * x
                n = n/2
            else:
                n = n -1
                ret *= x
        return ret*x

sol = Solution()
print(sol.myPow(2,9))