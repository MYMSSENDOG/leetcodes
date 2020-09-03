class Solution:
    def lcf(self, a, b):
        d = max(a,b)
        m = min(a,b)
        r = d % m
        while r != 0:
            t = r
            d = m
            m = t
            r = d % m
        return m
    def largestComponentSize(self, A) -> int:
        n = len(A)
        ret = 0
        mat = [[0] * n for _ in range(n)]
        visited = {}
        todo = [i for i in range(n)]
        for i in range(len(todo)):
            for j in range(i+1, n):
                if self.lcf(A[i], A[j]) != 1:
                    mat[i][j], mat[j][i] = 1,1


        for i in range(n):
            if i in visited:
                continue
            visited[i] = 1
            cur_ret = 1
            q = [i]
            while q:
                for _ in range(len(q)):
                    t = q.pop(0)
                    for next in range(n):
                        if mat[t][next] == 1 and next not in visited:
                            cur_ret += 1
                            visited[next] = 1
                            q.append(next)
            ret = max(ret, cur_ret)
        return ret






sol = Solution()
A = [2,3,6,7,4,12,21,39]
print(sol.largestComponentSize(A))
