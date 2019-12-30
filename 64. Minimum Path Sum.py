class Solution:
    def minPathSum(self, grid):
    #돌아가기 없음
        m = len(grid)
        if not m:
            return 0
        n = len(grid[0])
        board = [[9999999] * n for k in range(m)]
        board[0][0] = 0

        for i in range(m):
            for j in range(n):
                direction = []
                if i>0:
                    direction += [8]
                if j>0:
                    direction += [4]
                if i<m-1:
                    direction+= [2]
                if j<n-1:
                    direction+= [6]
                for d in direction:
                    if d == 8:
                        board[i-1][j] = min(board[i][j] + grid[i][j], board[i-1][j])
                    elif d == 2:
                        board[i+1][j] = min(board[i][j] + grid[i][j], board[i+1][j])
                    elif d == 4:
                        board[i][j-1] = min(board[i][j] + grid[i][j], board[i][j-1])
                    elif d == 6:
                        board[i][j+1] = min(board[i][j] + grid[i][j], board[i][j+1])
        return board[m-1][n-1] + grid[m-1][n-1]

n = [
  [1,1,98,98,98,98,98,98,98,98],
  [1,1,1,1,1,1,1,98,98,98],
  [98,98,98,98,98,98,1,98,98,98],
  [98,98,98,98,1,1,1,98,98,98],
  [98,98,98,98,1,98,98,98,98,98],
  [98,98,98,98,1,1,1,1,98,98],
  [98,98,98,98,98,98,1,1,1,1]
]

sol = Solution()
print(sol.minPathSum(n))