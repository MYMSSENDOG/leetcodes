# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = input().split(";")
table = [[int(i) for i in c.split()] for c in user_input]
ret = 0
m = len(table)
n = len(table[0])
for y in range(m):
    for x in range(n):
        if table[y][x] == 1:
            if x>0:
                ret += 1 if table[y][x-1] == 0 else 0
            if x < n-1:
                ret += 1 if table[y][x + 1] == 0 else 0
            if y > 0:
                ret += 1 if table[y - 1][x] == 0 else 0
            if y < m - 1:
                ret += 1 if table[y + 1][x] == 0 else 0
print(ret)
