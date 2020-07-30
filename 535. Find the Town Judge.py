import collections
class Solution:
    def findJudge(self, N: int, trust) -> int:
        d = collections.defaultdict(int)
        cand = {}
        for a, b in trust:
            d[b] +=1
            d[a] = False
        for i in range(1, N+1):
            if d[i] == N-1:
                if i not in cand:
                    return i
        return -1

sol = Solution()
N = 4
trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
print(sol.findJudge(N, trust))
