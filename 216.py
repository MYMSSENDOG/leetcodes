class Solution:
    def combinationSum3(self, k: int, n: int):
        def combine(n: int, k: int):
            if k == 0:
                return [[]]
            return [pre + [i] for i in range(k, n + 1) for pre in combine(i - 1, k - 1) ]
        ret =  combine(9,k)
        ret2 = []
        for r in ret:
            if sum(r) == n:
                ret2.append(r)
        return ret2
sol = Solution()
k = 3
n = 7
print(sol.combinationSum3(k, n))