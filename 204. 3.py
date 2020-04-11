class Solution:
    def countPrimes(self, n: int) -> int:
        p = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,
103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197]

        l = 0
        r = len(p)
        while l < r:
            m = (r + l) //2
            if p[m] ==n:
                return m
            elif p[m] > n:
                r = m
            elif p[m] < n:
                l = m+1
        return l
n = 6
sol = Solution()
print(sol.countPrimes(n))