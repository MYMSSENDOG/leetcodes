class Solution:
    def nthSuperUglyNumber(self, n: int, primes) -> int:
        size = len(primes)
        dp = [1]
        ugly_nums = [1] * size
        index = [0] * size
        for i in range(n-1):
            for k in range(size):
                if ugly_nums[k] == dp[-1]:
                    ugly_nums[k] = dp[index[k]] * primes[k]
                    index[k] +=1
            dp.append(min(ugly_nums))
        return dp[-1]







sol = Solution()
n = 2
primes = [2,3,5]
print(sol.nthSuperUglyNumber(n, primes))