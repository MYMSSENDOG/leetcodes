class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:

        def kmp():
            for i in range(1, sz):
                j = prefix[i - 1]
                while j != 0 and evil[i] != evil[j]:
                    j = prefix[j - 1]
                prefix[i] = j + 1 if evil[i] == evil[j] else 0

        def recurse(i, greater, smaller, ei):
            key = (i, greater, smaller, ei)
            if key in dp:
                res = dp[key]
            elif ei == len(evil):
                res = 0
            elif i == n:
                res = 1
            else:
                c1, c2, c3 = s1[i], self.s2[i], evil[ei]

                a, z = ord('a'), ord('z')
                st = a if greater else ord(c1)
                chars1 = range(st, z + 1)
                end = z if smaller else ord(c2)
                chars2 = range(a, end + 1)

                chars = set(chars1) & set(chars2)
                res = 0
                for ch in chars:
                    c = chr(ch)
                    ei2 = ei
                    while ei2 != 0 and evil[ei2] != c:
                        ei2 = prefix[ei2 - 1]
                    ei2 = (ei2 + 1) if c == evil[ei2] else 0

                    g2 = greater or (c > c1)
                    s2 = smaller or (c < c2)
                    res += recurse(i + 1, g2, s2, ei2)
                    res %= MOD
            dp[key] = res
            return res

        if s1 > s2:
            return 0

        dp = {}
        MOD = 10 ** 9 + 7
        self.s2 = s2
        sz = len(evil)
        prefix = [0] * sz
        kmp()
        return recurse(0, False, False, 0)
sol = Solution()
n = 3
s1 = "abc"
s2 = "bbc"
evil = "a"
print(sol.findGoodStrings(n, s1, s2, evil))