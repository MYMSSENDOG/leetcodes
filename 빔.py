input_line = input().split()

H = int(input_line[0])#높이
W = int(input_line[1])#넓이
mirror = [""  for i in range(H)]

for i in range(H):
    mirror[i] = input()
dir = [0,1]
y = 0
x = 0
ret = 0
while x>=0 and x< W and y >=0 and y <H:

    if mirror[y][x] == "-":
        pass
    else:
        if mirror[y][x] == "/":
            dir = [-dir[1],-dir[0]]
        elif mirror[y][x] == "\\":
            dir = [dir[1],dir[0]]
    ret += 1
    y += dir[0]
    x += dir[1]
print(ret)

