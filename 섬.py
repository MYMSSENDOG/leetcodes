input_line = input().split()

H = int(input_line[0])#height
W = int(input_line[1])#width
N = int(input_line[2])#number of island
map = []
dict = {}
for i in range(H):
    map.append([int(x) for x in input().split()])

minh = 999999
maxh = 0


def getIsland(h):
    ret = 0
    searched = [[False]*W for i in range(H)]
    four = [[0,1],[1,0],[-1,0],[0,-1]]
    for i in range(H):
        for j in range(W):
            if searched[i][j] or map[i][j]<=h:
                continue
            elif map[i][j] > h:
                ret +=1
                q = []
                searched[i][j] = True
                q.append([i,j])
                while q:
                    cur = q.pop(0)
                    for a,b in four:
                        x = cur[0] + a
                        y = cur[1] + b
                        if  x<0 or x >=H or y < 0 or y >= W or searched[x][y] :
                            continue
                        elif map[x][y] > h :
                            searched[x][y] = True
                            q.append([x,y])
    return ret


for i in range(H):
    for j in range(W):
        el = map[i][j]
        dict[el] = 1 if el in dict else 1
        minh = min(minh, el)
        maxh = max(maxh,el)
heights = []
for i in dict.keys():
    heights.append(i)
heights.sort()

if N == 1:
    print(0)
elif N == 0:
    print(maxh)
else:
    for i in heights:
        if getIsland(i) == N:
            print(i)
            break

