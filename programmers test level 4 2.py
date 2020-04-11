def solution(n):

    m = {(1,1) : 1}
    def dfs(l, r):
        if (l,r) in m:
            return m[(l,r)]
        if not l:
            m[(l,r)] = 1
            return m[(l,r)]
        ret = 0
        if l == r:
            ret = dfs(l-1, r)
            m[(l, r )] = ret
            return ret
        ret += dfs(l-1, r)
        ret += dfs(l, r-1)
        m[(l, r )] = ret
        return ret
    return dfs(n,n)



n = 5
print(solution(n))