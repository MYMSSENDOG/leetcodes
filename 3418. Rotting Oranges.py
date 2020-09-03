import collections
class Solution:
    def orangesRotting(self, grid) -> int:
        rotten = 0
        normal = 0
        m = len(grid)
        n = len(grid[0])
        d = collections.defaultdict(int)
        ret = 0
        q = []
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        for y in range(m):
            for x in range(n):
                d[(y,x)] = grid[y][x]
                if grid[y][x] == 1:
                    normal += 1
                if grid[y][x] == 2:
                    rotten +=1
                    q.append([y,x])

        if not rotten and not normal:
            return 0
        while q:
            ret+=1
            for _ in range(len(q)):

                y, x = q.pop(0)
                temp = []
                for dir in directions:
                    y_, x_ = dir
                    if d[(y+y_, x+x_)] == 1:
                        temp.append([y + y_, x + x_])
                if temp:
                    normal -= len(temp)
                    for y, x in temp:
                        q.append([y,x])
                        grid[y][x] = 2
                        d[(y,x)] = 2
        if normal != 0:
            return -1
        return ret -1









grid = [[2,1,1],[1,1,0],[0,1,1]]
sol = Solution()
print(sol.orangesRotting(grid))
