class Solution:
    def pacificAtlantic(self, matrix):
        m = len(matrix)
        if not matrix or not m:
            return []
        n = len(matrix[0])
        direction = [[0,1],[0,-1],[1,0],[-1,0]]
        dp = [[[0,0]for k in range(n)]  for _ in range(m)]  #0 pacific 1 atlantic
        q_p = [[0,i] for i in range(n)]
        q_a = [[m-1,i] for i in range(n)]
        q_p+=[[i,0]for i in range(1,m)]
        q_a += [[i, n-1] for i in range(m-1)]
        p_searched = {}
        a_searched = {}

        while q_p:
            for k in range(len(q_p)):
                y,x = q_p.pop(0)
                if (y,x) in p_searched:
                    continue
                else:
                    cur = matrix[y][x]
                    p_searched[(y,x)] = 1
                    dp[y][x][0] = 1
                    for b, a in direction:
                        ny = y+b
                        nx = x+a
                        if 0<= ny < m and 0<= nx < n and matrix[ny][nx] >= cur:
                            q_p.append([ny,nx])
        while q_a:
            for k in range(len(q_a)):
                y, x = q_a.pop(0)
                if (y,x) in a_searched:
                    continue
                else:
                    cur = matrix[y][x]
                    a_searched[(y,x)] = 1
                    dp[y][x][1] = 1
                    for b, a in direction:
                        ny = y+b
                        nx = x+a
                        if 0<= ny < m and 0<= nx < n and matrix[ny][nx] >= cur:
                            q_a.append([ny,nx])
        return [[i,j] for i in range(m) for j in range(n) if dp[i][j][0] == 1 and dp[i][j][1] == 1]







sol = Solution()
matrix = [[1,2],[4,3]]
print(sol.pacificAtlantic(matrix))