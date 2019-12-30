def perm(N):
    if len(N)==1:
        return [N]
    r = []
    for i in range(len(N)):
        s = N[:i] + N[i+1:]
        p = perm(s)
        for x in p:
            r.append(x + N[i:i+1])
    return r


def com(n, q):
    r = []
    if len(n) < q:
        return [[0]]
    elif len(n) == q:
        return [n]
    if q==1:
        for c in range(len(n)):
            r.append([])
            r[c].append(n[c])
        return r
    elif q==0:
        return [[0]]
    for i in range(len(n)):
        s = n[i]
        p = com(n[i+1:], q-1)
        for x in p :
            if 0 in x:
                pass
            else:
                r.append([s] + x)#[]빼던가넣던가
    return r

a = [1,2,3,4,5,6]
print(com(a,3))