class Solution:
    def countNegatives(self, grid) -> int:
        if not grid or not grid[0]:
            return 0
        m = len(grid)
        n = len (grid[0])
        ret = 0
        for row  in grid:
            for i, e in enumerate(row):
                if e <0:
                    ret+= n - i
                    break
        return ret
grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
sol = Solution()
print(sol.countNegatives(grid))