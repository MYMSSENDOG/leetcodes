class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        if n > 10:
            return 0
        def factorial(start, k):
            ret = start
            start -=1
            for _ in range(k-1):
                ret *= start
                start -= 1
            return ret

        ret = factorial(10,n)
        for i in range(1, n):# i = left zero
            zero_place = n - i - 1
            if zero_place>0:
                ret += zero_place * factorial(9,zero_place)
                if i > 1:
                    ret += factorial(9, zero_place + 1 )
            if zero_place == 0:
                if i > 1:
                    ret += 9
        if n >1:
            ret +=1
        return ret


sol = Solution()
n = 4
print(sol.countNumbersWithUniqueDigits(n))