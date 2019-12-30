class Solution:
    def isValidSudoku(self, board):
        #가로 검사 세로검사 박스검사
        valid = {}
        for i in range(9):
            valid.clear()
            for j in range(9):
                if board[i][j]==".":
                    continue
                if board[i][j] in valid:
                    return False
                else:
                    valid[board[i][j]] = 1


        for i in range(9):
            valid.clear()
            for j in range(9):
                if board[j][i]==".":
                    continue
                if board[j][i] in valid:
                    return False
                else:
                    valid[board[j][i]] = 1

        for i in range(3):
            for j in range(3):
                valid.clear()
                for k in range(3):
                    for l in range(3):
                        if board[i*3+k][j*3+l] == ".":
                            continue
                        if board[i * 3 + k][j * 3 + l] in valid:
                            return False
                        else:
                            valid[board[i * 3 + k][j * 3 + l]] = 1
        return True
input = [[".",".",".",".","5",".",".","1","."],
         [".","4",".","3",".",".",".",".","."],
         [".",".",".",".",".","3",".",".","1"],
         ["8",".",".",".",".",".",".","2","."],
         [".",".","2",".","7",".",".",".","."],
         [".","1","5",".",".",".",".",".","."],
         [".",".",".",".",".","2",".",".","."],
         [".","2",".","9",".",".",".",".","."],
         [".",".","4",".",".",".",".",".","."]]
sol = Solution()
print(sol.isValidSudoku(input))