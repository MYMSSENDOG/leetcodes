class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        i = len(obstacleGrid)
        if not i:
            return 0
        j = len(obstacleGrid[0])
        board = [[0]*j for k in range(i)]
        board[0][0] = 1

        for m in range(i):
            for n in range(j):
                if obstacleGrid[m][n] ==0:
                    if n>0 and m >0:
                        board[m][n] = board[m][n-1] + board[m-1][n]
                    elif n>0:
                        board[m][n] = board[m][n - 1]
                    elif m>0:
                        board[m][n] = board[m-1][n]
                else:
                    board[m][n] = 0
        return board[i-1][j-1]


n = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
sol = Solution()
print(sol.uniquePathsWithObstacles(n))