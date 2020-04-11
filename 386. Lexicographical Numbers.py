class Solution:
    def lexicalOrder(self, n: int) :
        ret = []
        def dfs(cur):
            ret.append(cur)
            cur *=10
            for i in range(10):
                if cur+i<=n:
                    dfs(cur+i)

        for i in range(1,10):
            if i <=n :
                dfs(i)
        return ret




sol = Solution()
n = 13
print(sol.lexicalOrder(n))