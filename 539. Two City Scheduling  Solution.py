import bisect
class Solution:
    def twoCitySchedCost(self, costs) -> int:
        L = []
        R = []
        ret = 0
        for l , r in costs:
            if l == r:
                ret += r
                continue
            if l > r:
                bisect.insort(R, l - r)
                ret+=r

            else:
                ret+=l
                bisect.insort(L,r - l)

        M, m = R ,L
        if len(R)<len(L):
            m,M = R, L
        dif = len(M) - len(m)
        ret += sum(M[:dif//2])
        return ret






costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
sol = Solution()
print(sol.twoCitySchedCost(costs))