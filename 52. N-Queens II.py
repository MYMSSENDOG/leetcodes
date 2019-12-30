class Solution:
    def totalNQueens(self, n: int) -> int:

        ret = []
        def dfs(queens, xysum, xydif):
            p = len(queens)
            if n == p:
                ret.append(1)
                return
            for q in range(n):
                if q not in queens and q+p not in xysum and p - q not in xydif:
                    dfs(queens + [q], xysum + [q+p], xydif + [p-q])
        dfs([],[],[])

        return len(ret)
sol = Solution()
print(sol.totalNQueens(4))
