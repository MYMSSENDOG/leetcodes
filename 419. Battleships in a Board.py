class Solution:
    def countBattleships(self, board) -> int:
        m = len(board)
        if not m:
            return 0
        n = len(board[0])
        ret = 0
        dir = [[0,1], [1, 0]]
        for i in range(m):
            for j in range(n):
                if board[i][j] == "X":
                    ret +=1
                    for d in dir:
                        ni, nj = i + d[0], j + d[1]
                        if 0<=ni<m and 0<=nj<n:
                            if board[ni][nj] == "X":
                                ret -=1

        return ret



sol = Solution()
board = ["X..X", "...X", "...X", "...X"]
print(sol.countBattleships(board))