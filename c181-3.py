"""

1 -
2 |
3 l b
4 b r
5 l t
6 r t

"""
import collections

class Solution:
    def hasValidPath(self, grid):
        d = {}
        for i in range(1,7):
            d[i] = {}
        d[1]["l"] = [0,1,"l"]
        d[1]["r"] = [0, -1, "r"]
        d[2]["b"] = [-1,0,"b"]
        d[2]["t"] = [1, 0, "t"]
        d[3]["l"] = [1,0,"t"]
        d[3]["b"] = [0, -1, "r"]
        d[4]["b"] = [0,1,"l"]
        d[4]["r"] = [1, 0, "t"]
        d[5]["l"] = [-1,0,"b"]
        d[5]["t"] = [0, -1, "r"]
        d[6]["r"] = [-1,0,"b"]
        d[6]["t"] = [0, 1, "l"]



        m = len(grid)
        if not grid or not m:
            return True
        n = len(grid[0])
        cur = (0, 0)
        cur_road = grid[cur[0]][cur[1]]
        if cur_road == 1 or cur_road == 3 or cur_road == 5:
            dir = "l"
        elif cur_road == 2 or cur_road == 6:
            dir = "t"
        else:
            dir = "r"
        dest = (m-1, n-1)
        s = collections.defaultdict(int)

        while 1:
            cur_road = grid[cur[0]][cur[1]]
            if dir not in d[cur_road]:
                return False
            if cur == dest:
                return True
            if cur in s:
                return False
            s[cur] = 1

            a, b, nd = d[cur_road][dir]
            cur = (cur[0] +a, cur[1] + b)

            dir = nd
            if not(0<=cur[0] < m) or not (0<=cur[1]<n):
                return False

sol = Solution()
grid = [[1,1,2]]
print(sol.hasValidPath(grid))