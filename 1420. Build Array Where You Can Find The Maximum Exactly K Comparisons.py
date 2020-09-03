class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        def nCr(n,r):
            r = min(r, n-r)
            ret = 1
            d = 1
            for i in range(r):
                ret *= n
                n-=1
                ret //= d
                d += 1
            return ret

        def helper(l, lo, hi, k):# lo <= x < hi
            mod = 10 ** 9 + 7
            if l < k or hi - lo < k:
                return 0
            if l == k:
                return nCr(hi - lo, k)
            if k == 0:
                return lo**l
            if k == 1:
                ret = 0
                for M in range(lo,hi):
                    for j in range(1, l+1):
                        ret += ((M**(l-j)) * ((lo - 1) ** (j-1)))%mod


                return ret
            left_k = k // 2
            ret = 0
            for left_len in range(1,l):
                for left_hi in range(lo,hi+1):
                    le = helper(left_len, lo, left_hi, left_k)% mod
                    ri = helper(l - left_len, left_hi + 1,hi, k - left_k)% mod
                    ret += (le * ri) % mod
                    ret = ret % mod
            return ret


        return helper(n,1,m+1,k)



sol = Solution()
n = 37
m = 17
k = 7
print(sol.numOfArrays(n,m,k))