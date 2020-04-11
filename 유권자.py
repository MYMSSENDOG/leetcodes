
M, N, K= input().split()
M = int(M)#후보자
N = int(N)#선거권자
K = int(K)#유세
array = [0]*(M+1)
q = {}
ret = [0]
for i in range(K):
    n = input()
    n = int(n)
    ntr = 0
    if N:
        N-=1
        ntr +=1
    for k in range(1,M+1):
        if array[k]:
            array[k] -=1
            ntr +=1
    array[n] += ntr
for i in range(1,M+1):
    if array[i] > array[ret[0]]:
        ret = [i]
    elif array[i] == array[ret[0]]:
        ret.append(i)
for i in ret:
    print(i)