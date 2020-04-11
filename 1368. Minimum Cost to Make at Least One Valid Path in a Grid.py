class Solution:
    def minCost(self, grid) -> int:

        m = len(grid)
        n = len(grid[0])
        not_searched = set()
        searched = set()
        for i in range(m):
            for j in range(n):
                not_searched.add((i,j))
        dp = [[999] * n for _ in range(m)]
        q = [(m-1, n-1)]
        nq = []
        cost = 0
        dp[-1][-1] = 0
        while not_searched:
            while q:
                for k in range(len(q)):
                    i,j = q.pop(0)
                    if (i,j) not in not_searched:
                        continue
                    not_searched.remove((i,j))
                    searched.add((i,j))
                    dp[i][j] = min(cost, dp[i][j])
                    directions= [(i,j-1), (i,j+1), (i-1,j), (i+1,j)]
                    for d, dir in enumerate(directions):
                        if dir in not_searched:
                            ni, nj = dir
                            if ni>=0 and ni <m and nj>=0 and nj<n:

                                if grid[ni][nj] == d + 1:
                                    q.append((ni, nj))
                                else:
                                    nq.append((ni, nj))
            q = nq
            nq = []
            cost+=1
        return dp[0][0]








sol = Solution()
grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
print(sol.minCost(grid))