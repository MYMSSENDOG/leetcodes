def is_normal(p):
    l = 0
    for c in p:
        if c == "(":
            l +=1
        else:
            l-=1
        if l < 0:
            return False
    return True

def solution(p):
    answer = ''
    if p =="":
        return p
    l = 0
    for i, e in enumerate(p):
        if e == "(":
            l+=1
        else:
            l-=1
        if l == 0:
            u = p[:i+1]
            v = p[i+1:]
            break
    if is_normal(u):
        return u + solution(v)
    else:
        s = "(" + solution(v)+")"
        u = u[1:-1]
        u2 = ""
        for i in u:
            if i == "(":
                u2 += ")"
            else:
                u2+="("
        return s + u2

p = ")("
print(solution(p))