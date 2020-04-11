input_line = input().split()


H = int(input_line[0])
W = int(input_line[1])
N = int(input_line[2])
board = [["."] * 22 for _ in range(22)]
directions = [[0,1],[0,-1],[1,0],[-1,0]]
def collide(start, end):
    pass
for i in range(H):
    input_line = input().split()
    for j in range(W):
        board[i+1][j+1] = input_line[j]
q = []
for i in range(N):
    input_line = input().split()
    q.append([int(k) for k in input_line])
for i in range(N):
    a,b,x,y = q[i]
    if board[a][b] != board[x][y]:
        print("no")
        continue
    if max(a,x) - min(a,x) + max(b,y) - min(b,y) == 1:
        print("yes")
        continue
    path1 = []
    path2 = []
    for d in directions:
        na = a
        nb = b
        while na<=1<=H and 1<=nb<=W:
            na+=d[0]
            nb+=d[1]
            if board[na][nb] == ".":
                path1.append([na, nb])
            else:
                break
        nx = x
        ny = y
        while 1<=nx<=H and 1<=ny<=W:
            nx+=d[0]
            ny+=d[1]
            if board[nx][ny] == ".":
                path2.append([nx, ny])
            else:
                break
    find = False
    for p1 in path1:
        p1a, p1b = p1
        for p2 in path2:
            p2a, p2b = p2
            if p1a != p2a and p1b != p2b:
                continue
            else:
                if p1a == p2a:
                    for k in range(min(p1b, p2b), max(p1b, p2b)+1):
                        if board[p1a][k] !=".":
                            break
                    else:
                        find = True
                        break
                elif p1b == p2b:
                    for k in range(min(p1a, p2a), max(p1a, p2a)+1):
                        if board[k][p1b] !=".":
                            break
                    else:
                        find = True
                        break
    if find:
        print("yes")
    else:
        print("no")
