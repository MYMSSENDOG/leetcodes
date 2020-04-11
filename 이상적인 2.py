N = int(input())#갯수
c = input().split()
c_f = int(c[0])#미래값
c_b = int(c[1])#과거값
a = input()#안전 불안 여부

r = [[]]
ret = [9999999]

def is_valide(route, i):
    c_bit = False
    for k in route:
        if k<i:
            c_bit = not c_bit
    if a[i] == "s":
        return not c_bit
    else:
        return c_bit

def helper(route, cost):
    if len(route) == N:#마지막으로 갈일만 남은 경우
        if N %2 == 1:
            if ret[0] > cost + c_f:
                r[0] = route + [N-1]
                ret[0]  = cost + c_f
            return
        else:
            cur_pos = route[-1]
            c = 999
            for i in range(cur_pos):
                if is_valide(route, i):
                    c = c_b
                    break
            for i in range(cur_pos+1, N):
                if is_valide(route, i):
                    c =  min(c, c_f)
                    break
            if ret[0] > cost + c + c_f:
                ret[0] = cost + c + c_f
                r[0] = route + [N-1]
    else:
        for i in range(N-1):
            temp_cost = c_b if i<= route[-1] else c_f
            if i not in route and is_valide(route, i):
                helper(route + [i], cost + temp_cost)
helper([N-1], 0)
for i in range(len(r[0])):
    r[0][i] +=1

s = str(N)
for i in r[0][1:]:
    s = s + " " + str(i)
print(s)