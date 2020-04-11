class Solution:
    def nthSuperUglyNumber(self, n: int, primes) -> int:
        if n == 1:
            return 1
        m = len(primes)

        ret = [[primes[0], 0]]
        for i in range(n-2):
            t = ret.pop(0)
            val = t[0]
            prod = t[1]
            if prod == m-1:
                ret.append([val * primes[m-1], m-1])
            else:
                l = 0
                r = len(ret)
                cur = val * primes[prod]
                mid = 0
                while l < r:
                    mid = (l + r) // 2
                    if ret[mid][0] > cur:
                        r = mid
                    else:
                        l = mid+1

                ret.insert(l, [cur, prod])
                r = len(ret)
                l =0
                cur = val * primes[prod+1]//primes[prod]
                while l < r:
                    mid = (l + r) // 2
                    if ret[mid][0] > cur:
                        r = mid
                    else:
                        l = mid+1

                ret.insert(l, [cur, prod+1])
            if len(ret) > n:
                ret.pop()

        return ret.pop(0)







sol = Solution()
n = 12
primes = [2,7,13,19]
print(sol.nthSuperUglyNumber(n, primes))