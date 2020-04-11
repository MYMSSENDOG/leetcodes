import sys
import math
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        two = 31
        three = 0
        five = 0
        M = sys.maxsize
        while M>=1:
            three +=1
            M //=3
        M = sys.maxsize
        log_max = math.log10(M)
        while M>=1:
            five +=1
            M //=5
        log = []
        l2 = math.log10(2)
        l3 = math.log10(3)
        l5 = math.log10(5)
        for i in range(two):
            for j in range(three):
                for k in range(five):
                    t = l2 * i + l3 * j + l5 * k
                    if t > log_max:
                        continue
                    log.append(t)
        log.sort()

        return int(10**log[n-1]+0.1)

sol = Solution()
n = 83
print(sol.nthUglyNumber(n))