def inspection(board, cur_pos, direction, stone):
    y, x = cur_pos
    y += direction[0]
    x += direction[1]
    rev = False
    dif = stone^1
    while 0<=x<=7 and 0<=y<=7:
        if board[y][x] == dif:
            rev = True
        elif board[y][x] == stone:
            if rev:
                return True
            return False
        elif board[y][x] == "N":
            return Falses
        y += direction[0]
        x += direction[1]
    return False
def rev_stone(board, cur_pos, direction, stone):
    y, x = cur_pos
    y += direction[0]
    x += direction[1]
    while 0<=x<=7 and 0<=y<=7 and board[y][x] != stone:
        board[y][x] = stone
        y += direction[0]
        x += direction[1]
K = int(input())
Board = [["N"]*8 for i in range(8)]
#Black 0 white 1
Board[3][3] = 1
Board[3][4] = 0
Board[4][3] = 0
Board[4][4] = 1
directions = [[1,0],[0,1],[-1,0],[0,-1],[1,1],[1,-1],[-1,-1],[-1,1]]
for i in range(K):
    input_line = input().split()
    stone = 0
    if "W" == input_line[0]:
        stone = 1
    row = int(input_line[1]) - 1
    col = int(input_line[2]) - 1
    Board[row][col] = stone
    for d in directions:
        if inspection(Board, [row, col], d, stone):
            rev_stone(Board, [row, col], d, stone)
w = 0
b = 0

for r in Board:
    w += r.count(1)
    b += r.count(0)
title = "black"
if w > b:
    title = "white"
if w != b:
    print(str(b) + "-" + str(w) + " The " + title + " won!")
else:
    print(str(b) + "-" + str(w) + " Draw!")