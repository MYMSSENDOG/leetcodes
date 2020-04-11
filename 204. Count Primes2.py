class Solution:
    def countPrimes(self, n: int) -> int:

        ret = 0
        sieve = [True] * n
        if n <3:
            return 0
        sieve[0] = False
        sieve[1] = False
        for i in range(2, n):
            if sieve[i] == True:
                ret +=1
                t = 2 * i
                while t < n:
                    sieve[t] = False
                    t += i
        return ret
n = 999999
sol = Solution()
print(sol.countPrimes(n))