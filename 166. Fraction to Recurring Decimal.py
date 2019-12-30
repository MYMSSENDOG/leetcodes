class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        n = int(numerator)
        d = int(denominator)
        if n == 0:
            return "0"
        minus = False
        if n^d <0:
            minus = True
        n = max(n,-n)
        d = max(d,-d)
        q = n // d
        r = n % d
        ret = ""
        if minus:
            ret += "-"
        ret += str(q)
        if r:
            ret += "."
        dict = []
        start = []
        while r:
            r *= 10
            q = r // d
            r = r % d
            if [q,r] in dict:
                start = [q,r]
                break
            dict.append([q, r])

        for i in dict:
            if i == start:
                ret += "("
            ret += str(i[0])
        if start:
            ret += ")"
        return ret

numerator = -50
denominator = 8
sol = Solution()
print(sol.fractionToDecimal(numerator, denominator))