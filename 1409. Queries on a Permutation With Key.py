class Solution:
    def processQueries(self, queries, m: int) :
        P = [i+1 for i in range(m)]
        ret = []
        for i in queries:
            idx = P.index(i)
            ret.append(idx)
            t = P.pop(idx)
            P = [t] + P
        return ret


sol = Solution()
queries = [3,1,2,1]
m = 5
print(sol.processQueries(queries, m))