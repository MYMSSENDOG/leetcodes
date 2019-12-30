class Solution:
    def solve(self, board: str) -> None:
        #1 연속된 O중 끄트머리에 닿지 않은 모든 것
        #2
        def helper(x, y):
            if x<0 or x>m-1 or y<0 or y >n-1:
                return
            if mark[x][y] == 1 or board[x][y] == "X":
                return
            else:
                mark[x][y] = 1
                q.append([x,y])

        m = len(board)
        n = len(board[0])
        mark = [[0]*n for i in range(m)]
        q = []

        for j in range(n):
            if board[0][j] == "O":
                q.append([0,j])
                mark[0][j] = 1
            if board[m-1][j] == "O":
                q.append([m-1, j])
                mark[m-1][j] = 1
        for i in range(1,m-1):
            if board[i][0] == "O":
                q.append([i,0])
                mark[i][0] = 1
            if board[i][n-1] == "O":
                q.append([i,n-1])
                mark[i][n-1] = 1
        while q:
            t = q.pop(0)
            x = t[0]
            y = t[1]
            helper(x+1,y)
            helper(x - 1, y)
            helper(x, y-1)
            helper(x,y+1)
        for i in range(m):
            for j in range(n):
                if mark[i][j] == 0:
                    board[i][j] = "X"
        return board
sol = Solution()
board = [["O","O","O"],["O","O","O"],["O","O","O"]]
print(sol.solve((board)))