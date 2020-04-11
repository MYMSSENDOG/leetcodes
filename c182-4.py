class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        prefix = ""

        for i in range(n):
            if s1[i] == s2[i]:
                prefix += s1[i]
        if evil in prefix:
            return 0
        def differnece(s11, s22):
            mult = 1
            n1, n2= 0, 0
            for i in range(n - 1, -1, -1):
                n1 += (ord(s1[i]) - ord("a")) * mult
                n2 += (ord(s2[i]) - ord("a")) * mult
                mult *= 26
            return n2 - n1

        ret = 0
        n1, n2, e1= 0,0,0
        mult = 1
        for i in range(n-1,-1,-1):
            n1 += (ord(s1[i]) - ord("a")) * mult
            n2 += (ord(s2[i]) - ord("a")) * mult
            mult *= 26
        mult = 1
        dif = n2 - n1 + 1
        for i in range(len(evil)-1, -1, -1):
            e1 += (ord(evil[i]) - ord("a")) * mult
            mult*=26






        return ret%(10 ** 9 + 7)

sol = Solution()
n = 2
s1 = "aa"
s2 = "da"
evil = "b"
print(sol.findGoodStrings(n,s1,s2,evil))