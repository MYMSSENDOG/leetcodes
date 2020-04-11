class Solution:
    def countPrimes(self, n: int) -> int:

        def isPrime(k):
            if k == 3 :
                prime.append(k)
                return True
            i = 0
            while prime[i] <= int(k ** (1/2)):
                if k %prime[i] == 0:
                    return False
                i +=1
            prime.append(k)
            return True


        prime = [2]
        if n<3:
            return 0
        elif n == 3:
            return 1

        i = 3
        ret = 1
        while i <n :
            if isPrime(i):
                ret +=1
            i +=2
        return ret

n = 99999
sol = Solution()
print(sol.countPrimes(n))