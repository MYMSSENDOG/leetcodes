N = int(input())#제품수
w = [0] * N
for i in range(N):
    w[i] = int(input())

M = int(input())# 방법 갯수
m = []# 무게 가격
for i in range(M):
    t = []
    t += [int(i) for i in input().split()]
    m.append(t)

max_weight = max(m)[0]
max_price = [999999] * (max_weight+1)
for i in range(len(m)):
    idx = m[i][0]
    v = m[i][1]
    max_price[idx] = min(max_price[idx], v)
prev = max_price[-1]
for i in reversed(range(max_weight)):
    if max_price[i] >= prev:
        max_price[i] = prev
    else :
        prev = max_price[i]

memo = {N:0}
def helper(start):
    if start in memo:
        return memo[start]
    if start == N-1:
        return max_price[w[start]]
    ret = 9999999
    s = start
    cur_sum = 0
    t = []
    while s < N and cur_sum + w[s]<=max_weight:
        cur_sum +=w[s]
        t.append(cur_sum)
        s +=1
    for sw in range(len(t)):
        ret = min(ret, max_price[t[sw]] + helper(start + sw + 1))
    memo[start] = ret
    return ret
print(helper(0))

