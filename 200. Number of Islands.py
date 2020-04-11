class Solution:
    def numIslands(self, grid) -> int:
        if not grid or not grid[0]:
            return 0
        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for i in range(m)]
        ret = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0" or visited[i][j] == True:
                    continue
                else:
                    q = [[i,j]]
                    visited[i][j] = True
                    ret +=1
                    while q:
                        for _ in range(len(q)):
                            t = q.pop(0)
                            ty = t[0]
                            tx = t[1]

                            if ty>0:
                                if grid[ty-1][tx] == "1" and not visited[ty-1][tx]:
                                    q.append([ty-1, tx])
                                    visited[ty - 1][tx] = True
                            if tx>0:
                                if grid[ty][tx - 1] == "1" and not visited[ty][tx-1]:
                                    q.append([ty, tx - 1])
                                    visited[ty][tx - 1] = True
                            if ty < m-1:
                                if grid[ty + 1 ][tx] == "1" and not visited[ty+1][tx]:
                                    q.append([ty+1, tx])
                                    visited[ty + 1][tx] = True
                            if tx <n-1:
                                if grid[ty][tx + 1] == "1" and not visited[ty][tx+1]:
                                    q.append([ty, tx+1])
                                    visited[ty][tx + 1]= True

        return ret
sol = Solution()
grid = ["11110","11010","11000","00000"]

print(sol.numIslands(grid))