import copy
def isValid(board,n):
    for i in range(n):
        for j in range(n):
            if board[i][j] != "Q":
                continue
            else:
                #가로 세로 대각선 밑으로 검증
                #그런데 가로는 안할거같은데.. 일단 넣음
                #가로
                for m in range(j,n):
                    if board[i][m] == "Q":
                        return False
                for m in range(i,n):
                    if board[m][j] == "Q":
                        return False
                k = j + 1
                m = i + 1
                while m<n and k < n:
                    if board[m][k] == "Q":
                        return False
                    m +=1
                    k+=1
                while m<n and k>=0:
                    if board[m][k] == "Q":
                        return False
                    m +=1
                    k -= 1
    return True
def mark(board, x,y, a):#a == 1 이면 Q 가 생기는거고 -1이면 Q제거
    n = len(board)
    for i in range(n):
        board[x][i] += a
        board[i][y] += a
    tx = x
    ty = y
    while tx>0 and ty > 0:
        tx -=1
        ty -=1
    while tx < n and ty < n:
        board[tx][ty] += a
        tx +=1
        ty +=1
    tx = x
    ty = y
    while tx<n-1 and ty > 0:
        tx +=1
        ty -=1
    while tx >=0  and ty < n:
        board[tx][ty] += a
        tx -= 1
        ty += 1
def placeQueen(board,validBoard,restQueen, ret):
    if restQueen == 1:
        if 0 in validBoard[-1]:
            board[-1] = board[-1][ : validBoard[-1].index(0)
                                                 ] + "Q" + board[-1][ validBoard[-1].index(0) + 1: ]
            temp = copy.deepcopy(board)
            ret.append(temp)
            board[-1] = board[-1][:validBoard[-1].index(0)] + "." + board[-1][validBoard[-1].index(0)+1:]
        return
    for i,x  in enumerate(validBoard[-restQueen]):
        if validBoard[-restQueen][i]==0:
#            board[len(board)-restQueen][i] = "Q"
            board[len(board) - restQueen] = board[len(board)-restQueen][:i] + "Q" + board[len(board) - restQueen][i+1:]
            mark(validBoard,len(board)-restQueen, i, 1)

            placeQueen(board,validBoard,restQueen-1,ret)

            board[len(board) - restQueen] = board[len(board) - restQueen][:i] + "." + board[len(board) - restQueen][i+1:]
            mark(validBoard, len(board) - restQueen, i, -1)
    return
class Solution:
    def solveNQueens(self, n: int):
        ret = []


        board = ["."* n for i in range(n)]
        validBoard = [[0] * n for i in range(n)]
        restOfQueen = n
        placeQueen(board, validBoard, restOfQueen, ret)

        return ret
        """
        valid보드에서 확인후 넣는다. 만약 마지막퀸이 넣을자리가 있으면 리턴에 추가, 없으면
        """

n = 5
sol = Solution()
a = sol.solveNQueens(n)
print(len(a))
for i in a:
    for j in i:
        print(j)
    print("")