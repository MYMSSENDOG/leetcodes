class Solution:
    def allPathsSourceTarget(self, graph):
        memo = {}
        n = len(graph)
        def helper(pos):
            ret = []
            if pos in memo:
                return memo[pos]
            for cand in graph[pos]:

                if cand == n-1:
                    ret += [[pos, n-1]]
                else:
                    ret += [[pos] + p for p in helper(cand)]

            memo[pos] = ret
            return ret
        helper(0)
        return memo[0]
graph = [[1,2], [3], [3], []]
sol = Solution()
print(sol.allPathsSourceTarget(graph))