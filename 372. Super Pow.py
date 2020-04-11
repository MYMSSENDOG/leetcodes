class Solution:
    def superPow(self, a: int, b) -> int:
        def gcd(a, b):
            s = max(a,b)
            t = min(a,b)
            if t == 0:
                return s
            while s%t !=0:
                s, t = t, s%t
            return t
        bb = 0
        m = 1
        for i in reversed(b):
            bb += i * m
            m *=10
        if gcd(a, 1337) == 1:
            bb %= 1140
            r = 1
            for _ in range(bb):
                r *= a
                r %= 1337
            return r
        else:

            remainders  = []
            r = a % 1337
            while not remainders or (remainders and r != remainders[0]):

                remainders.append(r)
                r *= a
                r %= 1337

            repeat = len(remainders)
            return remainders[bb % repeat-1]





a = 209253
b = [1,2,3,4]
sol = Solution()
print(sol.superPow(a,b))

