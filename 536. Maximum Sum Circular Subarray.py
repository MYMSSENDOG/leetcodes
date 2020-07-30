class Solution:
    def maxSubarraySumCircular(self, A) -> int:
        m = len(A)
        l = [0] * m
        r = [0] * m
        cur = 0
        r_max = A[0]
        if m == 1:
            return A[0]
        for i,e  in enumerate(A):
            cur += e
            r_max = max(cur, r_max)
            r[i] = r_max

        l_max = A[-1]
        cur = 0
        for i, e in enumerate(A[::-1]):
            cur += e
            l_max = max(l_max, cur)
            l[i] = l_max
        ret = max(l[i] + r[m - i - 2] for i in range(m-2))

        cur = 0
        mid_max = -99999
        for i in A:
            cur += i
            mid_max = max(mid_max, cur)
            if cur<0:
                cur = 0
        return max(mid_max, ret)


sol = Solution()
A = [5,-3,5]
print(sol.maxSubarraySumCircular(A))