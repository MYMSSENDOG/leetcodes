
h,w = input().split()
h = int(h)#선 길이7
w = int(w)#수직선 갯수4
n, m = input().split()
n = int(n)
m = int(m)
ret = [["_"] * w for i in range(h)]
p = [["_"]*n for i in range(m)]
for i in range(m):
    for j, e in  enumerate(input()):
        if e == "#":
            p[i][j] = "#"
q =  input()
q = int(q)
for i in range(q):
    x,y  = input().split()
    x = int(x)
    y = int(y)
    for a in range(n):
        for b in range(m):
            if p[a][b] == "#":
                ret[a+x-1][b+y-1] = "#" if ret[a+x-1][b+y-1] == "_" else "_"
for i in range(h):
    t = ""
    for j in range(w):
        t += ret[i][j]
    print(t)
