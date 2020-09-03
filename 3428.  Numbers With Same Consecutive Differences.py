class Solution:
    def numsSameConsecDiff(self, n: int, k: int):
        self.n = n
        self.k = k
        ret = []
        if n == 1:
            return [i for i in range(10)]
        if k == 0:
            m = 0
            for i in range(n):
                m = m*10 + 1
            return [i*m for i in range(1, 10)]
        for i in range(1, 10):
            ret += self.helper(i, n-1)
        return ret
    def helper(self,prev, n):
        if not n:
            return [prev]
        last = prev % 10
        ret = []

        if last + self.k <10:
            ret += self.helper(10 * prev + last + self.k, n-1)
        if last - self.k >= 0:
            ret += self.helper(10 * prev + last - self.k, n - 1)
        return ret


sol = Solution()
n = 3
k = 7
print(sol.numsSameConsecDiff(n, k))