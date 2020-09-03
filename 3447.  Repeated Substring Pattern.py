import collections
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        def lcf( a, b):
            d = max(a, b)
            m = min(a, b)
            r = d % m
            while r != 0:
                t = r
                d = m
                m = t
                r = d % m
            return m
        n = len(s)
        d = collections.defaultdict(int)
        mcd = 0
        for c in s:
            d[c] += 1

        for k,v in d.items():
            if not mcd:
                mcd = v
                continue
            mcd = lcf(mcd, v)
        if mcd == 1:
            if s.count(s[0]) == n:
                return True
            return False

        for i in range(mcd, 1, -1):
            if n % i != 0:
                continue
            size = n // i
            repeat = s[:size]
            l = size
            r = 2*size
            find = True
            while r <= n:
                if s[l:r] == repeat:
                    l =r
                    r += size
                    continue
                else:
                    find = False
                    break
            if find:
                return True
        return False

sol = Solution()
s= "abcabcabc"
print(sol.repeatedSubstringPattern(s))