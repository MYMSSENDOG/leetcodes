class Solution:
    def gameOfLife(self, board) -> None:
        if not board or not board[0]:
            return None
        m = len(board)
        n = len(board[0])
        q = [[0]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                count = 0
                u, d, l, r = False,False,False,False
                if i >0:
                    count += board[i - 1][j]
                    u = True
                if i < m-1:
                    count += board[i + 1][j]
                    d = True
                if j > 0:
                    count += board[i][j - 1]
                    l = True
                if j < n-1:
                    count += board[i][j + 1]
                    r = True

                if u and r:
                    count += board[i -1][j + 1]
                if u and l:
                    count += board[i - 1][j - 1]
                if d and r:
                    count += board[i + 1][j + 1]
                if d and l:
                    count += board[i + 1][j - 1]

                if board[i][j] == 1:
                    if count<2 or count>3:
                        q[i][j] = 1
                else:
                    if count == 3:
                        q[i][j] = 1
        for i in range(m):
            for j in range(n):
                board[i][j] ^= q[i][j]

        print(board)
board = [
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
sol = Solution()
print(sol.gameOfLife(board))


